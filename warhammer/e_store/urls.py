from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='product_list'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_details'),
        ]
