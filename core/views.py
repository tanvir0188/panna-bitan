from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    template = loader.get_template('core/contact.html')
    return HttpResponse(template.render())
