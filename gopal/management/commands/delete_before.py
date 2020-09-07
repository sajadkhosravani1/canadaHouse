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
        from django.utils.dateparse import parse_datetime
        from django.utils import timezone


        import pytz
        if options['date'][0] == "now":
            dt = timezone.now()
        else:
            try:
                dt = datetime.strptime(options['date'][0], Command.datetimeFormat)
            except ValueError:
                try: dt = datetime.strptime(options['date'][0], Command.datetimeFormat.split()[0])
                except ValueError:
                    raise ValueError("Incorrect date format, should be 'YYYY-MM-DD hh:mm:ss' or 'YYYY-MM-DD'")

            dt = timezone.get_current_timezone().localize(dt, is_dst=None)
        House.objects.filter(dateListed__lt=dt).delete()
