from rest_framework.serializers import ModelSerializer
from ..models import Clients, Departments

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'name', 'age', 'account_type', 'photo', 'department')

class DepartmentSerializers(ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'department_name')
