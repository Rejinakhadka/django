from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages


def index(request):
    products = Prouduct.objects.all()
    context = {
        'products':products
    }
    print(context['products'])
    return render(request,'products/index.html',context)

def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'products/addproduct.html',{
                'form':form
            })

    context = {
        'form':ProductForm
    }

    return render(request,'products/addproduct.html',context)

def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'products/addcategory.html',{
                'form':form
            })

    context = {
        'form':CategoryForm
    }
    return render(request,'products/addcategory.html',context)

