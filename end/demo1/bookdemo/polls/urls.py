# 引入路由绑定函数
from django.conf.urls import url
from . import views

app_name = "polls"

# 2,每一个路由文件中必须编写路由数组
urlpatterns = [
    # 使用正则分组可以向视图函数中传递参数
    # 第一个参数就是路由 第二个参数就是视图函数
    # 第一个参数中如果有正则分组 小括号 则正则分组匹配的内容会作为实参传递
    url(r'^pindex/$',views.pindex,name='pindex'),
    url(r'^pdetail/(\d+)/$',views.pdetail,name='pdetail'),
    url(r'^result/(\d+)/$',views.result,name='result'),



]