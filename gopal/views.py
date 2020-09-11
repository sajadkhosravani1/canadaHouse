from django.shortcuts import render,HttpResponse
from gopal.models import *


def home(request):
    context = {}
    return render(request,'gopal/home.html',context)
    pass


def list(request):
    houses = House.objects.all()

    if hasattr(request,'GET'):
        print(request.GET)
        if 'price_least' in request.GET.keys():
            houses = houses.filter(price__gt=int(request.GET['price_least']))
        if 'price_most' in request.GET.keys():
            houses = houses.filter(price__lt=int(request.GET['price_most']))
        if 'city' in request.GET.keys():
            houses = houses.filter(city=request.GET['city'])
        if 'state' in request.GET.keys():
            houses = houses.filter(city=request.GET['state'])

    for house in houses:
        ans = house.media_set.all()
        if len(ans) > 0:
            house.img_src = ans[0]
        else:
            house.img_src = None
    context = {
        'count': len(houses),
        'houses': houses,
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
        print(r)
        return HttpResponse(r.text)
    else:
        return HttpResponse("house with %d id details." % house_id)
    pass
