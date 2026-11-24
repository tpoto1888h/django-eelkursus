from django.http import HttpResponse
from django.template import loader
from .models import Book

def testing(request):
    mydata = Book.objects.filter(autor='Yu Mi').values()
    template = loader.get_template('template.html')
    context = {
        'mybooks': mydata,
    }
    return HttpResponse(template.render(context, request))

raamat = [
    {
        'pealkiri': 'Siinusteoreem',
        'autor': 'Max Mustermann',
        'saadavus': False,
    },
    {
        'pealkiri': 'Koosinusteoreem',
        'autor': 'Stirner Maximum',
        'saadavus': True,
    },
    {
        'pealkiri': 'Tangens',
        'autor': 'Henri Kuusk',
        'saadavus': False,
    },
    {
        'pealkiri': 'Kotangens',
        'autor': 'Ar siirius',
        'saadavus': True,
    },
]


def books(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'Minu raamatukogu',
        'raamatud': raamat,
    }

    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {'raamatud': raamat}
    return HttpResponse(template.render(context, request))

def available(request):
    template = loader.get_template('available.html')
    context = {
        'mybooks': Book.objects.filter(saadavus=True).values(),}
    return HttpResponse(template.render(context, request))