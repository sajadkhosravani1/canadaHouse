from django.core.management.base import BaseCommand, CommandError
from gopal.models import *


class Command(BaseCommand):
    help = 'Fetches data from API and put them into DB.'
    limit = 1000
    lazy = False
    priceRange = [0, 10_000_000_000]
    test = False # if test mode would be true, json objects will be read from cache file.

    def add_arguments(self, parser):
        parser.add_argument('limit', type=int, nargs=1, help='Objects\' max count to fetch.')

    def handle(self, *args, **options):
        Command.limit = options['limit'][0]
        objects = self.getObjects()
        if objects is None: return
        count = 0
        for dicObject in objects:
            try:
                houseId = int(dicObject['mlsListingID'][1:])
                if House.objects.filter(id=houseId).exists():
                    # In lazy mode we would assume that when we bump into a case that we have already saved that means
                    # we have already saved the rest. because the cases are sorted by date.
                    if Command.lazy:
                        break
                    else:
                        continue

                city = City(name=dicObject['city'])
                filtered = City.objects.filter(name=city.name)
                if not filtered.exists():
                    city.save()
                else:
                    city = filtered[0]

                state = State(name=dicObject['state'])
                filtered = State.objects.filter(name=state.name)
                if not filtered.exists():
                    state.save()
                else:
                    state = filtered[0]

                ownership = Ownership(value=dicObject['ownership'])
                filtered = Ownership.objects.filter(value=ownership.value)
                if not filtered.exists():
                    ownership.save()
                else:
                    ownership = filtered[0]

                lol_type = Type(name=dicObject['lolType'])
                filtered = Type.objects.filter(name=lol_type.name)
                if not filtered.exists():
                    lol_type.save()
                else:
                    lol_type = filtered[0]

                from django.utils.dateparse import parse_datetime
                dt = parse_datetime(dicObject['dateListed'])
                from django.utils import timezone
                dt = timezone.get_current_timezone().localize(dt, is_dst=None)
                house = House(
                    id=houseId, address=dicObject['address'],
                    city=city, state=state, ownership=ownership,
                    public_remarks=dicObject['publicRemarks'], price=dicObject['price'],
                    bedrooms=dicObject['bedrooms'], baths=dicObject['baths'],
                    dateListed=dt,
                    mediaURL=dicObject['mediaURL'],
                    size=dicObject['size']['low'], title=dicObject['title'],
                    office=dicObject['office'], lol_type=lol_type)
                house.save()
                for imgSrc in dicObject['media']:
                    Media(house=house, src=imgSrc).save()
                count += 1
            except: continue
        if count > 0:
            self.stdout.write(self.style.SUCCESS("%i new cases has been added successfully." % count))
        else:
            self.stdout.write(self.style.SUCCESS("No new case to add."))

    def getObjects(self):
        import json
        if Command.test:
            content = open('json.json', 'r').read()
        else :
            import requests
            from requests.exceptions import ConnectionError, HTTPError

            r = None
            try:
                r = requests.get(
                    """https://gopalsharma.ca/carmen-api/fvrebgv/carmen?limit=%i&price.gte=%i&price.lte=%i&latitude.gt=49.255846736035494&latitude.lt=49.311835132478706&longitude.gt=-123.2269100616455&longitude.lt=-123.01456493835448&sortBy=dateListed&order=desc""" \
                    % (Command.limit, *Command.priceRange))
                if r.status_code != 200:
                    r.raise_for_status()
                self.stdout.write(self.style.SUCCESS("Data has been received."))
                self.stdout.write("It may take couple of minutes to parse and write data into our local database.")

            except ConnectionError:
                self.stderr.write("Connection error")
                return None
            except HTTPError as e:
                self.stderr.write(str(e))
                return None
            content = r.text

        return json.loads(content)['bundle']