from django.shortcuts import render

from item.models import Category, Item

def index(request):
    items = Item.objects.all()[0:3]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories, 
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')