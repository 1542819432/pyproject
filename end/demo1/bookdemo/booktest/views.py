from django.shortcuts import render, redirect, reverse
from django.template import loader
from .models import Book, Hero

# Create your views here.

# MVT V视图函数 3个作用 接受请求 处理请求 返回响应


# 3编写对应的视图函数
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    # # return HttpResponse("这里是首页")
    # # 1获取模板
    # template = loader.get_template('index.html')
    # # 2渲染模板数据
    books = Book.objects.all()
    # context = {"books":books}
    # result = template.render(context)
    # # 3将渲染结果使用HttpResponse返回
    # return HttpResponse(result)

    # 3合一
    return render(request, 'index.html', {"books": books})


def detail(request, bookid):
    # # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # constext = {"book":book}
    # result = template.render(constext)
    # return HttpResponse(result)

    return render(request, 'detail.html', {"book": book})


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect(redirect_to='/')
    return redirect(to='/')

def addbook(request):
    if request.method == "GET":
        return render(request,'addbook.html')
    elif request.method == "POST":
        book = Book()
        book.title = request.POST.get("bookname")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        # url = reverse("booktest:addbook")
        return redirect(to="/")

def editbook(request,bookid):
    book = Book.objects.get(id=bookid)

    if request.method == "GET":
        return render(request,'editbook.html',{"book":book})
    elif request.method == "POST":
        book.title = request.POST.get("bookname")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        return redirect(to="/")

def deletehero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()

    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    if request.method == "GET":
        return render(request,'addhero.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:addhero",args=(bookid,))
        return redirect(to=url)

def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)

    if request.method == "GET":
        return render(request,'edithero.html',{"hero":hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)



def about(request):
    return HttpResponse("这里是关于")

# 使用django 模板
# MVT
