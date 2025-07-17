from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Clients,Departments
from .Form import ClientForm , DepartmentForm

def Home(request):
    people=Clients.objects.all()
    return render(request,'app/index.html',{'people':people})
 
def clientForm(request):
    if request.method == 'POST': 
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app')  
    else:
        form = ClientForm()
    return render(request, 'app/form.html', {'form': form})
  
def departmentForm(request):
    if request.method == 'POST': 
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app/department')  
    else:
        form = DepartmentForm()
    return render(request, 'app/form.html', {'form': form})

def DeleteClient(request, clientID):
    client = get_object_or_404(Clients, pk=clientID)
    client.delete() 
    return redirect('/app')  

def EditClient(request, clientID):
    client = get_object_or_404(Clients, pk=clientID)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/app')   
    else:
        form = ClientForm(instance=client)

    return render(request, 'app/form.html', {'form': form})

def Department(request):
    dept =Departments.objects.all()
    people=Clients.objects.all()
    return render(request,'app/Department.html',{'dept':dept,'people':people})

def DeleteDepartment(request,departmentID):
    dept=get_object_or_404(Departments,pk=departmentID)
    dept.delete()

def EditDepartment(request,departmentId):
    dept=get_object_or_404(Departments,pk=departmentId)

    if request=="POST":
        form=DepartmentForm(request.post,request.file,instance=dept)
        if form.is_valid:
            form.save()
            return redirect('/app')
    else:
        form=DepartmentForm()
    
    return render(request,'app/form.html',{'form':form})

