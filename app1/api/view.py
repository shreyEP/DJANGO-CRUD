from rest_framework.viewsets import ModelViewSet
from ..models import Clients, Departments
from .serializer import ClientSerializer, DepartmentSerializers

class ClientViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

class DepartmentViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializers
