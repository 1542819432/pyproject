from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from .models import *

from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from django.contrib.auth import authenticate, login as lin, logout as lot


# Create your views here.

def pindex(request):
    titles = Title.objects.all()

    return render(request, 'pindex.html', {"titles": titles})


class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "pindex.html"
    # queryset 指明返回的结果列表
    queryset = Title.objects.all()
    # context_object_name 指明返回字典参数的键
    context_object_name = "titles"

    # 方法一、继承的TemplateView
    # template_name = "pindex.html"
    # def get_context_data(self, **kwargs):
    #     return {"titles":Title.objects.all()}


def pdetail(request, titleid):
    if request.method == "GET":
        if request.user and request.user.username !="":
            # 已经登录过
            try:
                title = Title.objects.get(id=titleid)
                if title in request.user.titles.all():
                    print("已经投过票")
                    url = reverse("polls:result",args=(titleid))
                    return redirect(to=url)
                else:
                    try:
                        # title = Title.objects.get(id=titleid)
                        return render(request, 'pdetail.html', {"title": title})
                    except Exception as e:
                        print(e)
                        return HttpResponse("问题不合法")
            except Exception as e:
                print(e,"----")

        else:
            url = reverse("polls:login")+"?next=/polls/pdetail/"+titleid+"/"
            return redirect(to=url)
    elif request.method == "POST":
        optionid = request.POST.get("num")
        try:
            option = Option.objects.get(id=optionid)
            option.num += 1
            option.save()
            request.user.titles.add(Title.objects.get(id=titleid))
            url = reverse("polls:result", args=titleid)
            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


def result(request, oid):
    try:
        titles = Title.objects.get(id=oid)
        return render(request, 'result.html', {"titles": titles})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 可以使用django自带的用户认证系统 认证成功返回用户 失败返回None
        user = authenticate(username=username, password=password)
        # 调用Django登录方法 其实是为了生成cookie
        if user:
            lin(request, user)
            next = request.GET.get("next")
            if next:
                url = next
            else:
                url = reverse("polls:pindex")
            return redirect(to=url)
        else:
            url = reverse("polls:login")
            return redirect(to=url)


def logout(request):
    lot(request)
    url = reverse("polls:pindex")
    return redirect(to=url)


def regist(request):
    if request.method == "GET":
        return render(request,'regist.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).count()>0:
            return HttpResponse("用户名已存在")
        else:
            if password == password2:
                User.objects.create_user(username=username,password=password)
                url = reverse("polls:login")
                return redirect(to=url)
            else:
                return HttpResponse("密码不一致")




