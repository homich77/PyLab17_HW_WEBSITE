from django.shortcuts import render
from django.views.generic import ListView, DetailView
from e_store.models import *


class ProductListView(ListView):
    template_name = 'e_store/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'e_store/product.html'
    model = Product
    context_object_name = 'product'
