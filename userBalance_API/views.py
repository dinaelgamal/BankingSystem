from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status


class userBalanceAPIView(APIView):
    def get(self, request , userID):
        try:
            model = userInfo.objects.get(userID=userID)
            bSerializer = userBalanceSerializer(model)
        except:
            return Response("User Does not Exist", status=status.HTTP_404_NOT_FOUND)

        return Response(bSerializer.data)


