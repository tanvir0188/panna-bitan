from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('core/contact.html')
    return HttpResponse(template.render())
