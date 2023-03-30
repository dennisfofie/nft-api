from django.urls import path
from nft_api.views import ListCreateView, SearchNft, Top10NftView, NftDetailView

urlpatterns = [
    path("", ListCreateView.as_view(), name="list-nft"),
    path("search/", SearchNft.as_view(), name="search-nft"),
    path("top-10/", Top10NftView.as_view(), name="top-10"),
    path("nft/<uuid:pk>/", NftDetailView.as_view(), name="nft-detail"),
]
