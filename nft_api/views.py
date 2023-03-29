from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nft_api.serializer import NftSerializer
from nft_api.models import Nft


# Create your views here.
class ListApiView(APIView):
    serializer_class = NftSerializer

    def get(self, request, *args, **kwargs):
        data = Nft.objects.all()
        serializer = self.serializer_class(instance=data, many=True)
        response = {
            "result": "success",
            "counts": len(serializer.data),
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)
