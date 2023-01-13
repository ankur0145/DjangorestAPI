from rest_framework import Serializers
from rest_framework import ProductMain
from .models import ProductMain,ProductColour,ProductImage

class ProductMainSerializer(Serializers.ModelSerializer):
    class Meta:
        Model=ProductMain
        fields='get_all_product'

class ProductColurSerializer(Serializers.ModelSerializer):
    class Meta:
        Model=ProductColour
        fields='red,blue,green,black'
class ProductImageSerializer(Serializers.ModelSerializer):
    class Meta:
        Model=ProductImage
        fields='Image'

class ProductMainSerializer(Serializers.ModelSerializer):
    class Meta:
        Model=ProductMain
        fields='all_product_details'
