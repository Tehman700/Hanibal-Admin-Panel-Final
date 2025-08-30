from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="product_images/", storage=S3Boto3Storage())
    description = models.TextField()
    category = models.CharField(max_length=100)
    is_hot = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name
