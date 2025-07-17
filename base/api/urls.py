from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.api.url import pr

router = DefaultRouter()
router.registry.extend(pr.registry)   
urlpatterns = [
    path('', include(router.urls)),   
]
