from django.db import models

from django.contrib.auth.models import User

class Expands(models.Model):

    text=models.CharField(max_length=255)
    date=models.DateTimeField('date')
    amount=models.BigIntegerField()
    user=models.ForeignKey(User)





