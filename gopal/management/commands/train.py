from django.core.management.base import BaseCommand
from gopal.models import House

class Command(BaseCommand):
    help = 'Deletes all records before a specific date.'
    # DEFAULT_PERCENT = 80 # default train set percent.

    def add_arguments(self, parser):
        parser.add_argument('percent', nargs=1, type=int,
                            help="""Train set percentage.(Is 80 by default).""")

    def handle(self, *args, **options):
        x = []
        y = []

        for house in House.objects.all():
            x.append([house.bedrooms,house.baths,house.size,
                      house.lol_type.id,house.state.id,house.city.id,house.ownership.id])
            y.append(house.price)

        from sklearn import linear_model
        regr = linear_model.LinearRegression()
        regr.fit(x, y)

        import pickle
        # save in houses_trained.pkl
        with open('houses_trained.pkl', 'wb') as f:
            pickle.dump(regr, f)

        # load
        # with open('model.pkl', 'rb') as f:
        #     clf2 = pickle.load(f)

        self.stdout.write(self.style.SUCCESS(str(options['percent'][0])))

