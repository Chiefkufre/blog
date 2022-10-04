from ast import LShift
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
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            _name = form.cleaned_data['name']
            _new_list = ToDoList(name=_name)
            _new_list.save()
        else:
            pass
        
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})


def list_view(response, id):
    ls = ToDoList.objects.get(id=id)
    items = ls.items_set.all() 
    if response.method == "POST":
        if response.POST.get('save'):
            for item in items:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                new_text =ls.items_set.create(text=txt, complete=False)
                new_text.save()
        elif response.POST.get("deleteItem"):
            for item in items:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    ls.items_set.delete( )
                


        
        # form = CreateNewList(response.POST)

    
    return render(response, "main/list.html", {"ls":ls, "items": items})
