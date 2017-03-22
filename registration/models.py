from django.db import models
from django.utils import timezone
from django.conf import settings

class content_id(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    content_ids = models.ManyToManyField(content_id)
    course_time = models.TimeField(auto_now=False, auto_now_add=False)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_instructor')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='course_student')
    
    def __str__(self):
        return self.name
        
# Create your models here.
