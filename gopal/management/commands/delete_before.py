from django.core.management.base import BaseCommand
from gopal.models import House

class Command(BaseCommand):
    help = 'Deletes all records before a specific date.'
    datetimeFormat = '%Y-%m-%d %H:%M:%S'

    def add_arguments(self, parser):
        parser.add_argument('date', nargs=1, type=str,
                            help="""Date and time with %s format.
                             Dates in '%s' format are acceptable too."""\
                %('YYYY-MM-DD hh:mm:ss','YYYY-MM-DD'))

    def handle(self, *args, **options):
        from datetime import datetime
        from django.utils import timezone

        if options['date'][0] == 'now':
            dt = timezone.now()
        else:
            try:
                dt = datetime.strptime(options['date'][0], Command.datetimeFormat)
            except ValueError:
                try: dt = datetime.strptime(options['date'][0], Command.datetimeFormat.split()[0])
                except ValueError:
                    raise ValueError("Incorrect date format, should be 'YYYY-MM-DD hh:mm:ss' or 'YYYY-MM-DD'")

            dt = timezone.get_current_timezone().localize(dt, is_dst=None)
        filtered = House.objects.filter(dateListed__lt=dt)
        count = filtered.count()
        if count == 0:
            self.stdout.write(self.style.SUCCESS("There is nothing to delete with entered condition."))
        elif input("%i cases to delete. Are you sure?"%count).lower().startswith('y'):
            filtered.delete()
            self.stdout.write(self.style.SUCCESS("%i cases has been deleted successfully."%count))
        else:
            print("Nothing has been deleted.")


