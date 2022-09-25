from django.contrib import admin

# Register your models here.
from .models import Items, ToDoList

admin.site.register(ToDoList)