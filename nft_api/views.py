from django.shortcuts import render
from rest_framework import status, filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from nft_api.serializer import NftSerializer
from nft_api.models import Nft
from django_filters.rest_framework import DjangoFilterBackend
from .filters import NftFilters


# Create your views here.
class ListCreateView(APIView):
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

    def post(self, request, *args, **kwargs):
        context = {"request": request, "user": request.user}
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {"status": "success", "data": serializer.data}
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchNft(generics.ListAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer
    filterset_class = NftFilters
    search_fields = ["ratingAverage", "price", "name"]
    ordering_fields = "__all__"
