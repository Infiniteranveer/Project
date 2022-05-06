from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.


def home(request):
    return render(request,'index.html')


def createProject(request):
    form = ProjectForm()
    context = {'form':form}
    return render(request,"project_form.html",context)
