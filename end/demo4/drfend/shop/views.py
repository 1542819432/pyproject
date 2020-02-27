# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import *
# # django本身自带的序列化
# from django.core import serializers
#
#
# # Django 本身就可以完成前后端分离时开发 为前端提供json数据返回 但是django本身的序列化太麻烦 几乎没人用
# # 使用DRF框架可以提供方便的序列化操作
# def index(request):
#     # 如果以jaon或者xml的形式返回数据，则可以实现前后端分离开发
#     categorys = Category.objects.all()
#     result = serializers.serialize("json", categorys)
#     print(result)
#     return JsonResponse(result, safe=False)
#
#     # 如果使用Django模板就是前后端不分离
#     # return render(request,'模板名字',传递参数)


from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer

