from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects', views.projects_view, name="projects"),
    path('project_<int:project_id>/', views.project_view, name="project"),
    path('thingys', views.thingys_view, name="thingys"),
]