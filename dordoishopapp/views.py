import dordoishopapp
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from dordoishopapp.forms import UserForm,DordoiShopForm,UserFormForEdit, ProductForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login  

from dordoishopapp.models import Product

def home(request):
    return redirect(dordoishop_home)

@login_required(login_url='dordoishopapp/sign-in')
def dordoishop_home(request):
       return redirect(dordoishop_product)


@login_required(login_url='dordoishopapp/sign-in')
def dordoishop_account(request):
    user_form = UserFormForEdit(request.POST, instance=request.user)
    dordoishop_form = DordoiShopForm(request.POST, request.FILES,instance=request.user.dordoishop)
    
    if request.method == 'POST':
        user_form = UserFormForEdit(instance=request.user)
        dordoishop_form = DordoiShopForm(instance=request.user.dordoishop)

        if user_form.is_valid() and dordoishop_form.is_valid():
            user_form.save()
            dordoishop_form.save()

    return render(request,'dordoishopapp/account.html',{
        'user_form': user_form,
        'dordoishop_form':dordoishop_form
    })

@login_required(login_url='dordoishopapp/sign-in')
def dordoishop_product(request):
    products = Product.objects.filter(dordoishop=request.user.dordoishop).order_by("-id")
    return render(request,'dordoishopapp/product.html',{
        'products':products
    })

@login_required(login_url='dordoishopapp/sign-in')
def dordoishop_add_product(request):
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.dordoishop = request.user.dordoishop
            product.save()
            return redirect(dordoishop_product)

    return render(request,'dordoishopapp/add_product.html',{
        'form':form
    })

@login_required(login_url='dordoishopapp/sign-in')
def dordoishop_edit_product(request,product_id):
    form = ProductForm(instance=Product.objects.get(id=product_id))
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=Product.objects.get(id=product_id))
        if form.is_valid():
            product = form.save()
            return redirect(dordoishop_product)

    return render(request,'dordoishopapp/edit_product.html',{
        'form':form
    })



def dordoishop_sign_up(request):
    user_form = UserForm()
    dordoishop_form = DordoiShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        dordoishop_form = DordoiShopForm(request.POST, request.FILES)

        if user_form.is_valid() and dordoishop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_dordoishop = dordoishop_form.save(commit=False)
            new_dordoishop.owner = new_user
            new_dordoishop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(dordoishop_home)
    return render(request,'dordoishopapp/sign_up.html', {
        'user_form':user_form,
        'dordoishop_form':dordoishop_form
    })

