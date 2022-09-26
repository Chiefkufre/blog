from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ToDoList, Items
from .forms import CreateNewList


def index(response):

    return render(response, 'main/base.html', {})


def home(response, id):

    ls = ToDoList.objects.get(id=id)

    items = ls.items_set.all()

    return render(response, 'main/home.html', {"items": items, "ls": ls})


def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
