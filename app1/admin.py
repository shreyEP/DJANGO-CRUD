from django.contrib import admin

# Register your models here.
from .models import Clients,Departments 

admin.site.register(Clients)
admin.site.register(Departments) 