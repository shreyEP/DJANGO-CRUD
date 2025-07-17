from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("This is About")