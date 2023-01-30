from django.db import models

# Create your models here.
class Infoss(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/uploads")




