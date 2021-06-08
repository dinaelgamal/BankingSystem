from django.db import models
from django.db.models.fields import related
from userBalance_API.models import userInfo

class transactions(models.Model):
    senderID = models.ForeignKey(userInfo, null = True , related_name='sender' ,on_delete=models.CASCADE)
    receiverID = models.ForeignKey(userInfo,  null = True ,related_name='receiver', on_delete=models.CASCADE)
    transferAmount = models.FloatField()
    currency = models.CharField(max_length=5)

