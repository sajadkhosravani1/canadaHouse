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
        print(request.GET)
        if len(houses)>0 and 'price_least' in request.GET.keys() and len(request.GET['price_least']):
            print('price_least:',request.GET['price_least'])
            houses = houses.filter(price__gt=int(request.GET['price_least']))
        if len(houses)>0 and 'price_most' in request.GET.keys() and len(request.GET['price_most']):
            print('price_most:',request.GET['price_most'] )
            houses = houses.filter(price__lt=int(request.GET['price_most']))
        if len(houses)>0 and 'city' in request.GET.keys() and len(request.GET['city']):
            print('city:',request.GET['city'])
            houses = houses.filter(city=City.objects.get(name=request.GET['city']))
        if len(houses)>0 and 'state' in request.GET.keys() and len(request.GET['state']):
            print('state:',request.GET['state'])
            houses = houses.filter(state=State.objects.get(name=request.GET['state']))

    if len(houses) == 0: empty = True

    for house in houses:
        ans = house.media_set.all()
        # if len(ans) > 0:
        #     house.img_src = ans[0]
        # else:
        house.img_src = None
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
    context = {}
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
