from django.shortcuts import render

from .models import Title, Option


# Create your views here.

def pindex(request):
    titles = Title.objects.all()

    return render(request, 'pindex.html', {"titles": titles})


def pdetail(request, titleid):
    title = Title.objects.get(id=titleid)
    if request.method == "GET":
        return render(request, 'pdetail.html', {"title": title})


def result(request, oid):
    title = Option.objects.get(id=oid).title
    option = Option.objects.get(id=oid)
    option.num = option.num + 1
    option.save()
    return render(request, 'result.html', {"title": title})
