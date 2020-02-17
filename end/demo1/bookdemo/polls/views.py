from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from .models import Title, Option

from django.views.generic import View,TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView

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
        try:
            title = Title.objects.get(id=titleid)
            return render(request, 'pdetail.html', {"title": title})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    elif request.method == "POST":
        optionid = request.POST.get("num")
        try:
            option = Option.objects.get(id=optionid)
            option.num+=1
            option.save()
            url = reverse("polls:result",args=titleid)
            return redirect(to=url)
        except:
            return HttpResponse("选项不合法")


def result(request,oid):
    try:
        titles = Title.objects.get(id=oid)
        return render(request,'result.html',{"titles":titles})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")


