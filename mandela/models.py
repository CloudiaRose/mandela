from django.db import models

# Create your models here.
# mandela/models.py
from django.db import models

class Biography(models.Model):
    content = models.TextField()
    

class Quote(models.Model):
    content = models.TextField()
    source = models.CharField(max_length=100)

class Legacy(models.Model):
    content = models.TextField()
