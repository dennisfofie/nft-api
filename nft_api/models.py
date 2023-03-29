from django.db import models
import uuid

# Create your models here.


class Nft(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    maxGroupSize = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=50)
    ratingAverage = models.DecimalField(decimal_places=1, max_digits=2)
    ratingQuantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    summary = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    imgCover = models.ImageField(upload_to="nft/images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class NftImages(models.Model):
    nft_image = models.ImageField(upload_to="nft/nft_", blank=True, null=True)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE, related_name="nft_images")

    def __str__(self):
        return self.nft
