from django.db import models
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
# can be removed once I have templates for the other pages
from django.http import HttpResponse
from django.template import loader

from .models import Project, ProjectImage

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my homepage!")

def projects_view(request):
    project_list = Project.objects.order_by("-date")
    for p in project_list:
        p.main_image = ProjectImage.objects.filter(project=p.id)
    context = {
        'project_list':project_list
    }
    return render(request, "portfolio/index.html", context)

def project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        "project":project
    }
    
    return render(request, "portfolio/project.html", context)

def thingys_view(request):
    return HttpResponse("This is the page to 'show off' some code thingy(s)")
