from django.db import models

from django.contrib.auth.models import User

class Expenses(models.Model):

    text=models.CharField(max_length=255)
    date=models.DateTimeField('date')
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        mydate=self.date.strftime("%Y-%m-%d")
        return ("{} - {}".format(mydate,self.amount))


class Incoms(models.Model):

    text=models.CharField(max_length=255)
    date=models.DateTimeField('dates')
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        mydate=self.date.strftime("%Y-%m-%d")
        return ("{} - {}".format(mydate,self.amount))



