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

        test_set_percent = int(options['percent'][0])/100
        train_set_len = int(len(x)*test_set_percent)

        from sklearn import linear_model
        from sklearn.metrics import r2_score
        regr = linear_model.LinearRegression()
        regr.fit(x[:train_set_len], y[:train_set_len])

        import pickle
        # save in houses_trained.pkl
        with open('houses_trained.pkl', 'wb') as f:
            pickle.dump(regr, f)

        score = r2_score(y[train_set_len:], regr.predict(x[train_set_len:]))
        self.stdout.write(self.style.SUCCESS("r2 score: "+str(score)))

