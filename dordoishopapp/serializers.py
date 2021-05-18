from django.db.models import fields
from django.http import request
from rest_framework import serializers
from dordoishopapp.models import DordoiShop, Product

class DordoiShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self,dordoishop):
        request = self.context.get('request')
        logo_url = dordoishop.logo.url
        return request.build_absolute_uri(logo_url)
    class Meta:
        model = DordoiShop
        fields = ('id', 'name', 'phone', 'address', 'logo')


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self,product):
        request = self.context.get('request')
        image_url = product.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Product
        fields = ('id', 'name', 'short_description', 'image', 'price')
