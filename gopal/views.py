from django.shortcuts import render,HttpResponse

app_name = 'gopal'


def home(request):
    return HttpResponse("What do you want to do?")
    pass


def list(request):
    print(request.GET)
    return HttpResponse("houses")
    pass


def estimate(request):
    return HttpResponse("Price estimating.")
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
