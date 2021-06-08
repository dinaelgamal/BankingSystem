from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from userBalance_API.models import userInfo
from rest_framework import status

class userTransferAPIView(APIView):
    def post(self, request):
        amount = request.data['transferAmount']
        currency = request.data['currency'] 
        tSerializer = userTransferSerializer(data=request.data)

        try:
            senderID = request.data['senderID']
            senderUser = userInfo.objects.get(pk=senderID)
                
        except:
            return Response("Sender User Does not Exist", status=status.HTTP_404_NOT_FOUND)
            
        try:
            receiverID = request.data['receiverID']
            receiverUser = userInfo.objects.get(pk=receiverID)
                
        except:
            return Response("Receiver User Does not Exist", status=status.HTTP_404_NOT_FOUND)

        if senderUser.userAccountBalance >= amount:
            if currency == 'USD':
                receiverUser.userAccountBalance = receiverUser.userAccountBalance + (amount *15)
                receiverUser.save()
            else:
                receiverUser.userAccountBalance = receiverUser.userAccountBalance + amount 
                receiverUser.save()
            if currency == 'USD':
                senderUser.userAccountBalance = senderUser.userAccountBalance - (amount *15)
                senderUser.save()
            else:
                senderUser.userAccountBalance = senderUser.userAccountBalance - amount 
                senderUser.save()
        else:
            return Response("Account Balance Is Not Enough", status=status.HTTP_406_NOT_ACCEPTABLE)

        if tSerializer.is_valid():
            tSerializer.save()
            return Response(tSerializer.data, status = status.HTTP_200_OK)
        