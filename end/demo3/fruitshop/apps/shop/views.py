from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, Page

# Create your views here.
from .models import *


def index(request):
    goods = Goods.objects.all()

    return render(request, 'index.html', locals())


def detail(request, goodsid):
    try:
        goods = Goods.objects.get(id=goodsid)
        return render(request, 'shop.html', locals())
    except Exception as e:
        print(e)
        return HttpResponse("商品不合法")


def about(request):
    return render(request, 'about-us.html')


def account(request):
    return render(request, 'my-account.html')


def shop(request):
    goods = Goods.objects.all()
    paginator = Paginator(goods, 8)
    paginators = Paginator(goods, 6)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    pages = paginators.get_page(num)

    return render(request, 'shop.html', locals())


def shopsingle(request):
    return render(request, 'shop-single.html')


def contact(request):
    return render(request, 'contact.html')
