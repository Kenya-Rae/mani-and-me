from django.shortcuts import render

# Create your views here.

def view_shopping_bag(request):
    """ View to return the shopping bag """

    return render (request, 'bag/shopping_bag.html')