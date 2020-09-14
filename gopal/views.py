from django.shortcuts import render,HttpResponse
from gopal.models import *


def home(request):
    context = {}
    return render(request,'gopal/home.html',context)
    pass


def list(request):
    houses = House.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    empty = False

    if hasattr(request,'GET'):
        if len(houses)>0 and 'price_least' in request.GET.keys() and len(request.GET['price_least']):
            houses = houses.filter(price__gt=int(request.GET['price_least']))
        if len(houses)>0 and 'price_most' in request.GET.keys() and len(request.GET['price_most']):
            houses = houses.filter(price__lt=int(request.GET['price_most']))
        if len(houses)>0 and 'city' in request.GET.keys() and len(request.GET['city']):
            houses = houses.filter(city=City.objects.get(name=request.GET['city']))
        if len(houses)>0 and 'state' in request.GET.keys() and len(request.GET['state']):
            houses = houses.filter(state=State.objects.get(name=request.GET['state']))

    if len(houses) == 0: empty = True

    for house in houses:
        ans = house.media_set.all()
        if len(ans) > 0:
            house.img_src = ans[0]
        else:house.img_src = None
    context = {
        'count': len(houses),
        'houses': houses,
        'states': states,
        'cities': cities,
        'empty': empty
    }
    return render(request,'gopal/list.html',context)
    pass


def estimate(request):
    context = dict()
    context["states"] = [state.name for state in State.objects.all()]
    context["cities"] = [city.name for city in City.objects.all()]
    context['types'] = [type.name for type in Type.objects.all()]
    context['ownerships'] = [item.value for item in Ownership.objects.all()]

    if request.method=="POST":

        for key, value in request.POST.items():
            print(key,value)
            context[key] = value
        del context['csrfmiddlewaretoken']

        with open('houses_trained.pkl', 'rb') as f:
            import pickle
            regr = pickle.load(f)
            predicted = regr.predict([
                [int(context['bedrooms']), int(context['baths']), int(context['size']),
                Type.objects.get(name=context['type']).id, State.objects.get(name=context['state']).id,
                City.objects.get(name=context['city']).id, Ownership.objects.get(value=context['ownership']).id]])
            context['predicted_price'] = int(predicted[0])

    return render(request,'gopal/estimate.html',context)
    pass


def house_view(request,house_id):
    import requests
    r = requests.get('https://gopalsharma.ca/listing/R'+str(house_id))
    if r.status_code == 200:
        return HttpResponse(r.text)
    else:
        return HttpResponse("house with %d id details." % house_id)
    pass
