from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to return homepage """

    return render (request, 'home/index.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def contact_us(request):
    return render(request, 'home/contact_us.html')