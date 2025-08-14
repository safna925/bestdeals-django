from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model (Extending Django Default User)
class User(AbstractUser):
    email = models.EmailField(unique=True)

# Flipkart Product Model
class Flipkart(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='flipkart_images/')
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    reviews = models.TextField()

    def _str_(self):
        return f"{self.product_name} - {self.brand}"

# Amazon Product Model
class Amazon(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='amazon_images/')
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    reviews = models.TextField()

    def _str_(self):
        return f"{self.product_name} - {self.brand}"

# Unified Product Model for Comparison

"""class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=100)
    description = models.TextField()

    # Amazon Data
    amazon_price = models.CharField(max_length=50)
    amazon_reviews = models.CharField(max_length=10)
    amazon_image = models.ImageField(upload_to='amazon_images/')
    amazon_url = models.URLField()

    # Flipkart Data
    flipkart_price = models.CharField(max_length=50)
    flipkart_reviews = models.CharField(max_length=10)
    flipkart_image = models.ImageField(upload_to='flipkart_images/')
    flipkart_url = models.URLField()

    def _str_(self):
        return self.name"""
