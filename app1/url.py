
from django.urls import path,include
from . import views

urlpatterns = [ 
    path('',views.Home,name='home'), 
    path('addClients/',views.clientForm,name='form'),
    path('edit/<int:clientID>/', views.EditClient, name='edit_person'),
    path('delete/<int:clientID>/', views.DeleteClient, name='delete_person'),
    path('department/', views.Department, name='see_dept'),
    path('department/addDepartment/', views.departmentForm, name='dept_form'),
    path('department/delete/<int:departmentID>/',views.DeleteDepartment,name='delete_department'),
    path('department/edit/<int:departmentID>/',views.EditDepartment ,name='edit_department')
]