from distutils.command.upload import upload
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    link = models.TextField()
    photo = models.ImageField(upload_to = "media/events")
    
    def __str__(self):
        return self.name
    
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to = "media/members")
    
    def __str__(self):
        return self.name