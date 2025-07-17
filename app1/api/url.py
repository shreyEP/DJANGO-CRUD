from django.urls import path
from rest_framework.routers import DefaultRouter
from .view import ClientViewSet, DepartmentViewSet

pr = DefaultRouter()
pr.register(r'clients', ClientViewSet)        
pr.register(r'departments', DepartmentViewSet) 