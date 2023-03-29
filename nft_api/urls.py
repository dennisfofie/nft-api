from django.urls import path
from nft_api.views import ListCreateView, SearchNft

urlpatterns = [
    path("", ListCreateView.as_view(), name="list-nft"),
    path("search/", SearchNft.as_view(), name="search-nft"),
]
