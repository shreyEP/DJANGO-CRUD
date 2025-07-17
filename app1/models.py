from django.db import models
from django.utils import timezone  
# Create your models here.


class Departments(models.Model):
    department_name = models.CharField(max_length=50, unique=True,default=None)

    def __str__(self):
        return self.department_name



class Clients(models.Model):
    TYPE = [
        ('st', 'Students'),
        ('t', 'Teachers'),
    ]
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    account_type = models.CharField(max_length=5, choices=TYPE)
    photo = models.ImageField(upload_to='images/',blank=True,null=True)
    
    # Add this line to assign one department to a client
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return self.name

      
