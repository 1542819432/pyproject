from django.contrib import admin

from .models import Title,Option
from django.contrib.admin import ModelAdmin
# Register your models here.


class OptionInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Option
    extra = 5

class OptionAdmin(ModelAdmin):
    list_display = ('choice',)

    # 定义搜索字段
    search_fields = ('choice', )


admin.site.register(Option,OptionAdmin)

class TitleAdmin(ModelAdmin):
    """
    定义模型管理
    通过该类可以修改后台界面
    """
    # 更改后端显示
    list_display = ('name',)

    # 定义搜索字段
    search_fields = ('name',)

    inlines = [OptionInline]

admin.site.register(Title,TitleAdmin)