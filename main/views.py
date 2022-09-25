from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import ToDoList, Items


def index(response):

    return render(response, 'main/base.html', {})


def home(response):

    return render(response, 'main/home.html', {})

    # return HttpResponse("<h1>%s</h1><h2>%s</h2><ul>%s</ul>" %(items.text, items.complete, ls.name))
