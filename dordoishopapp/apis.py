import dordoishopapp
from django.http import JsonResponse

from .models import DordoiShop, Product
from dordoishopapp.serializers import DordoiShopSerializer,ProductSerializer

def client_get_dordoishops(request):
    dordoishops = DordoiShopSerializer(
    DordoiShop.objects.all().order_by('-id'),
    many=True,
    context={'request':request}
    ).data

    return JsonResponse({'dordoishops':dordoishops})

def client_get_products(request,dordoishop_id):
    products = ProductSerializer(
        Product.objects.all().filter(dordoishop_id=dordoishop_id).order_by('-id'),
        many=True,
        context={'request':request}
    ).data
    return JsonResponse({'products':products})