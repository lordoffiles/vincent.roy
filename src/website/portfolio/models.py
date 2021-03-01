from django.db import models
from jsonfield import JSONField

# Create your models here.

class Project(models.Model):
    # blank=True --> field can be blank
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    tags = JSONField(null=True)
    #images through FK
    date = models.DateField('Date', blank=True, null=True)
    link = models.URLField(max_length=500, blank=True)
    technologies = JSONField(null=True)

    def __str__(self):
        return "{} :: {}".format(self.title, self.description[:50])


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="image_project_name", on_delete=models.CASCADE)
    image = models.FileField(upload_to="uploads/")
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        p = Project.objects.get(id__exact=self.project.id)
        main_text = "Main Image ::" if self.is_main_image else ""
        return "{} :: {} {}".format(p.title, main_text, self.image.name)