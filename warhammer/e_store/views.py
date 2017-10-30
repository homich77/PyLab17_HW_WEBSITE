from django.shortcuts import render
from django.views.generic import ListView, DetailView
from e_store.models import *


class CategoryListView(ListView):
    template_name = 'e_store/category_list.html'
    model = Category
    context_object_name = 'categories'


class ProductListView(DetailView):
    template_name = 'e_store/product_list.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=context['category'])
        return context


class ProductDetailView(DetailView):
    template_name = 'e_store/product.html'
    model = Product
    context_object_name = 'product'
