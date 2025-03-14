from django.db import models

# Create your models here.

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.FileField(upload_to="project_images/", blank=True)
    url = models.CharField(max_length=100, default='')
    testimonial_text = models.CharField(max_length=500, default='')
    testimonial_name = models.CharField(max_length=200, default='')
    testimonial_avatar = models.FileField(upload_to="project_images/", blank=True)
    testimonial_url = models.CharField(max_length=100, default='')