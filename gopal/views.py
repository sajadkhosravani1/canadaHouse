from django.shortcuts import render,HttpResponse

app_name = 'gopal'


def home(request):
    context = {}
    return render(request,'gopal/home.html',context)
    pass


def list(request):
    # request.GET
    context = {}
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
