from django.db import models

# Create your models here.
class List (models.Model):
    item = models.CharField(max_length= 250)
    completed = models.BooleanField(default= False)


    def __str__(self):
        return self.item
