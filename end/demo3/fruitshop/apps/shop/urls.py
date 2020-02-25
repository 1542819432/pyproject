from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^account/$', views.account, name='account'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shopsingle/$', views.shopsingle, name='shopsingle'),
    url(r'^contact/$', views.contact, name='contact'),

]