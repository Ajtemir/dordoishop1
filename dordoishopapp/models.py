# from dordoishopapp.forms import DordoiShopForm
# from dordoishopapp.views import dordoishop_product
from django.db import models
from django.contrib.auth.models import User

class DordoiShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dordoishop')
    name = models.CharField(max_length=100,verbose_name='Опишите каким продовольствием занимаетесь?')
    phone = models.CharField(max_length=100, verbose_name='Ваш номер:')
    address = models.CharField(max_length=100, verbose_name='Адрес:')
    logo = models.ImageField(upload_to='dordoishop_logo/',blank=False,verbose_name='Ваш контейнер или фото вашего ассортимента?')

    def __str__(self):
        return self.name

class Product(models.Model):
    dordoishop = models.ForeignKey(DordoiShop,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/',blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='client')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.get_full_name()



