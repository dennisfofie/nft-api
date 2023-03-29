from django_filters import rest_framework as filters
from nft_api.models import Nft


class NftFilters(filters.FilterSet):
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    rating = filters.NumberFilter(field_name="ratingAverage", lookup_expr="exact")
    summary = filters.CharFilter(field_name="summary", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Nft
        fields = ["price", "name", "ratingAverage", "summary", "description"]
