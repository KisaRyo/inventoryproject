from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import  Product, Orders
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.db import models
from datetime import date, time
from django.utils import timezone
from user.views import PasswordsChangeView

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@login_required
def index(request):
    orders = Orders.objects.all().order_by('date','time')
    products = Product.objects.all().order_by('name')
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    orders_count = Orders.objects.all().count()

    pfilter = ProductFilter(request.GET, queryset=products)
    products = pfilter.qs

    paginator = Paginator(products,5)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
        'pfilter':pfilter,  
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items_count = Product.objects.all().count()
    orders_count = Orders.objects.all().count()
    context={
        'workers': workers,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context={
        'workers':workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    items = Product.objects.all().order_by('name')
    items_count = items.count()
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count = User.objects.all().count()
    orders_count = Orders.objects.all().count()


    pfilter = ProductFilter(request.GET, queryset=items)
    filtered_items = pfilter.qs

    paginator = Paginator(filtered_items,6)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)


    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            product_specification = form.cleaned_data.get('specifications')
            messages.success(request, f'{product_name} ({product_specification}) has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'items_count':items_count,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'pfilter': pfilter,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method =='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):

    current = date.today

    orders = Orders.objects.order_by('date', 'time')
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()

    paginator = Paginator(orders, 6)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            messages.success(request, f'Schedule has been added')
            return redirect('dashboard-order')
    else:
        form = OrderForm()
    context={
        'orders':orders,
        'form':form,
        'orders_count':orders_count,
        'workers_count':workers_count,
        'items_count':items_count,
        'curennt':current,
    }
    return render(request, 'dashboard/order.html', context)

@login_required
def order_delete(request, pk):
    orders = Orders.objects.get(id=pk)
    if request.method=='POST':
        orders.delete()
        return redirect('dashboard-order')
    return render(request, 'dashboard/order_delete.html')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)
