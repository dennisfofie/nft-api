from django.urls import path
from nft_api.views import ListApiView

urlpatterns = [
    path("", ListApiView.as_view(), name="list-nft"),
]
