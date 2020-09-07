from django.core.management.base import BaseCommand, CommandError
from gopal.models import *

class Command(BaseCommand):

    help = 'Fetches data from API and put them into DB.'
    limit = 1000
    priceRange = [500_000, 1_000_000]

    def handle(self, *args, **options):

        objects = self.getObjects()
        if objects is None: return
        count = 0
        for dicObject in objects:
            houseId = int(dicObject['mlsListingID'][1:])
            if House.objects.filter(id=houseId).exists():
                # When we bump into a case that we have already saved that means
                # we have already saved the rest. because the cases are sorted by date.
                break

            city = City(name = dicObject['city'])
            res = City.objects.filter(name=city.name)
            if not res.exists(): city.save()
            else : city = res[0]

            state = State(name = dicObject['state'])
            res = State.objects.filter(name=state.name)
            if not res.exists(): state.save()
            else: state = res[0]

            ownership = Ownership(value=dicObject['ownership'])
            res = Ownership.objects.filter(value=ownership.value)
            if not res.exists(): ownership.save()
            else: ownership = res[0]

            lol_type = Type(name=dicObject['lolType'])
            res = Type.objects.filter(name=lol_type.name)
            if not res.exists(): lol_type.save()
            else: lol_type = res[0]

            from datetime import datetime

            house = House(
                id=houseId, address=dicObject['address'],
                city=city, state=state, ownership=ownership,
                public_remarks=dicObject['publicRemarks'], price=dicObject['price'],
                bedrooms=dicObject['bedrooms'], baths=dicObject['baths'],
                dateListed=datetime.strptime(dicObject['dateListed'], '%Y-%m-%d %H:%M:%S'),
                mediaURL=dicObject['mediaURL'],
                size=dicObject['size']['low'], title=dicObject['title'],
                office=dicObject['office'], lol_type = lol_type)

            for imgSrc in dicObject['media']:
                Media(house=house, src=imgSrc ).save()
            count += 1

        if count > 0:
            self.stdout.write(self.style.SUCCESS("%i new cases has been added successfully."%count))
        else:
            self.stdout.write(self.style.SUCCESS("No new case to add."))






    def getObjects(self):

        import requests
        from requests.exceptions import ConnectionError, HTTPError
        import json
        #
        # r = None
        # try:
        #     r = requests.get(
        #         """https://gopalsharma.ca/carmen-api/fvrebgv/carmen?limit=%i&price.gte=%i&price.lte=%i&latitude.gt=49.255846736035494&latitude.lt=49.311835132478706&longitude.gt=-123.2269100616455&longitude.lt=-123.01456493835448&sortBy=dateListed&order=desc%20HTTP/1.1""" \
        #         % (Command.limit, *Command.priceRange))
        #     if r.status_code != 200:
        #         r.raise_for_status()
        # except ConnectionError:
        #     self.stderr.write("Connection error")
        #     return None
        # except HTTPError as e:
        #     self.stderr.write(str(e))
        #     return None
        # content = r.text

        content = open('json.json','r').read()

        return json.loads(content)['bundle']

