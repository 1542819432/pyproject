from django.contrib import admin

from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import Book,Hero,User

class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 5

class HeroAdmin(ModelAdmin):
    list_display = ('name','gender','content','book')

    # 定义搜索字段
    search_fields = ('name','gender','content' )
    # 指定过滤字段
    list_filter = ('name','gender','content','book' )



admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    """
    定义模型管理
    通过该类可以修改后台界面
    """
    # 更改后端显示
    list_display = ('title','price','pub_date')
    # 分页
    # list_per_page = 1

    # 定义搜索字段
    search_fields = ('title','price')
    # 指定过滤字段
    list_filter = ('title','price',)
    inlines = [HeroInline]

admin.site.register(Book,BookAdmin)

admin.site.register(User)



