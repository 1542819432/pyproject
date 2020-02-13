from django.shortcuts import render
from django.template import loader
from .models import Book,Hero

# Create your views here.

# MVT V视图函数 3个作用 接受请求 处理请求 返回响应


# 3编写对应的视图函数
from django.http import HttpResponse
def index(resquest):
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
    return render(resquest,'index.html',{"books":books})


def detail(resquest,bookid):
    # # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # constext = {"book":book}
    # result = template.render(constext)
    # return HttpResponse(result)

    return render(resquest,'detail.html',{"book":book})

def about(resquest):
    return  HttpResponse("这里是关于")

# 使用django 模板
# MVT
