"""dordoi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dordoishopapp import views,apis

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dordoishopapp/sign-in/', auth_views.LoginView.as_view(template_name='dordoishopapp/sign_in.html'),
    name='dordoishopapp-sign-in'),

    path('dordoishopapp/sign-out/', auth_views.LogoutView.as_view(next_page='/'),
    name='dordoishopapp-sign-out'),

    path('dordoishopapp',views.dordoishop_home,name='dordoishop_home'),

    path('dordoishopapp/sign-up',views.dordoishop_sign_up,name='dordoishop-sign-up'),

    path('dordoishopapp/account/',views.dordoishop_account,name='dordoishop-account'),

    path('dordoishopapp/product/',views.dordoishop_product,name='dordoishop-product'),

    path('dordoishopapp/product/add',views.dordoishop_add_product,name='dordoi-add-product'),

    path('dordoishopapp/product/edit/<int:product_id>/',views.dordoishop_edit_product,name='dordoishop-edit-product'),
    # API's

    path('api/client/dordoishops',apis.client_get_dordoishops),
    path('api/client/products/<int:dordoishop_id>/',apis.client_get_products),
    # sign in out up
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # convert token in up

    # revoke token
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
