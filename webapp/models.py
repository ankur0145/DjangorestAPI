from django.db import models

class ProductMain(models.Model):
    titlename=models.CharField(max_length=10)
    Description=models.CharField(max_length=10)
    Price=models.IntegerField(max_length=10)
    Size=models.IntegerField(max_length=10)
    Quality=models.CharField()


class ProductColour(models.Model):
    ProductColour=models.ForeignKey


class ProductImage(models.Model):
    ProductImage=models.CharField(max_length=10)

