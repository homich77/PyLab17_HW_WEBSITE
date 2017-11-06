from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
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


class ProductOrderView(TemplateView):
    template_name = 'e_store/product.html'

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_create(status='open')[0]
        item_id = request.POST['product_id']
        Order.objects.create(order=cart, item=Product.objects.get(pk=item_id),
                             quantity=int(request.POST['quantity']))
        cart.save()
        return HttpResponseRedirect('/store/cart')


class CartView(ListView):
    model = Cart
    context_object_name = 'orders'
    template_name = 'e_store/cart.html'

    def get_queryset(self):
        cart = Cart.objects.filter(status='open')
        if cart:
            orders = Order.objects.filter(order=cart)
            return orders
        return False

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart = Cart.objects.filter(status='open')
        if cart:
            orders = Order.objects.filter(order=cart)
            total = 0
            for order in orders:
                total += order.order_price
            context['sum'] = total
        return context


class CartPayView(TemplateView):
    template_name = 'e_store/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(status='open')
        if cart:
            cart.status = 'closed'
            cart.save()
        return HttpResponseRedirect('/store/cart')
