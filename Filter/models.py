from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.TextField(max_length=100, null= True)
    releasedate = models.DateField()
    readcount = models.IntegerField()
