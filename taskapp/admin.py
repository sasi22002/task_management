# admin.py
from django.contrib import admin
from .models import Task,User

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'dueDate', 'completed']
    ordering = ['dueDate']

admin.site.register(Task, TaskAdmin)



class TMSUser(admin.ModelAdmin):
    list_display = ['email', 'username']

admin.site.register(User, TMSUser)
