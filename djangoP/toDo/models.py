from django.db import models

# Create your models here.
class toDOItem(models.Model):
    text = models.CharField(max_length=60, blank=False)

