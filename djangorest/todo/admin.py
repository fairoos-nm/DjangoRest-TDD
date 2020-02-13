from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    """
    This class define the admin config for the model todo.
    """
    list_display = ('title', 'description', 'completed')

#Model registration
admin.site.register(Todo, TodoAdmin)
