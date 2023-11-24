from django.db import models


class LotteryNumber(models.Model):
    #number = models.IntegerField()
    number = models.CharField(max_length=2)
    def __str__(self):
        return str(self.number)
