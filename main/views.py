from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import ToDoList, Items


def index(response):

    return HttpResponse("something nice")


def intro(response, id):

    # ls = ToDoList.objects.get(id=id)
    items = Items.objects.get(id=id)
    ls = ToDoList.objects.get(id=id)

    return JsonResponse({

        "Items": items.text,
        "Status": items.complete,
        "name": ls.name

    })

    # return HttpResponse("<h1>%s</h1><h2>%s</h2><ul>%s</ul>" %(items.text, items.complete, ls.name))
