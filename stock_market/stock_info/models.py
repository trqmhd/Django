from django.db import models
import django.db.models.fields
from user_info.models import UserProfileInfo
from django.conf.urls import url, include

#from .views import StockDetailView


# Create your models here.

class StockInfo(models.Model):

    symbol = models.CharField(max_length=10)
    date = models.DateField()
    high = models.DecimalField(max_digits=15, decimal_places=7, null=True)
    low = models.DecimalField(max_digits=15, decimal_places=7, null=True)
    open = models.DecimalField(max_digits=15, decimal_places=7, null=True)
    close = models.DecimalField(max_digits=15, decimal_places=7, null=True)
    volume = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    adj_close = models.DecimalField(max_digits=15, decimal_places=7, null=True)
    #user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)#




    def get_absolute_url(self):
        return ("{}".format(self.id))

    def __str__(self):
        return self.symbol

