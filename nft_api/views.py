from django.shortcuts import render
from rest_framework import status, filters, generics, mixins
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
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NftDetailView(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = NftSerializer
    queryset = Nft.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SearchNft(generics.ListAPIView):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer
    filterset_class = NftFilters
    search_fields = ["ratingAverage", "price", "name"]
    ordering_fields = "__all__"


class Top10NftView(generics.ListAPIView):
    serializer_class = NftSerializer
    queryset = Nft.objects.all().order_by("-ratingAverage")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:10]
