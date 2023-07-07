from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=60)
    contact=models.CharField(max_length=10)