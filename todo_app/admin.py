from django.contrib import admin
from .models import ToDoItems, ToDoList


# Register your models here.
@admin.register(ToDoItems)
class ToDoItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'todo_list']


admin.site.register(ToDoList)
