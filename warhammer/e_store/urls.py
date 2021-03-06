from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^(?P<pk>\d+)/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^([0-9]+)/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_details'),
    url(r'^([0-9]+)/(?P<pk>\d+)/order/$', view=views.ProductOrderView.as_view(), name='product_order'),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),
    url(r'^cart/pay/$', views.CartPayView.as_view(), name='cart_pay'),
        ]
