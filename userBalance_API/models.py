from django.db import models

class userInfo(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=200)
    userAccountID = models.IntegerField()
    userAccountBalance = models.FloatField()