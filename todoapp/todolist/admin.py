from django.contrib import admin
from todolist.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'due_date']