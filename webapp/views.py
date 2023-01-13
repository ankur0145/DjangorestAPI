from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import status
from . models import ProductMain,ProductColour,ProductImage
from.Serializers import ProductMainSerializer

class ProductList(APIView):
    def get(self,request):
        ProductMain1=ProductMain.objects.all()
        Serializers=ProductMainSerializer(ProductMain1,many=True)
        return Response(serializer.data)
    def post(self):
        pass




