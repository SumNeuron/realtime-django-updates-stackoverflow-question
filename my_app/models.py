from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class MyQuery(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    total = models.IntegerField(default=0)
    date = models.DateTimeField('date created')
    def __str__(self):
        return self.date + ":\t" + str(self.a) + " + " + str(self.b)
