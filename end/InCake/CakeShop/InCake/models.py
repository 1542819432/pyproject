from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品中文名称")
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name="商品描述")
    price = models.FloatField(verbose_name="商品价格")
    weight = models.FloatField(verbose_name="商品规格")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类", related_name="goods")

    def __str__(self):
        return self.name


class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg',verbose_name="商品展示图")
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name="商品",related_name='imgs')

    def __str__(self):
        return self.good.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name="手机号")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", related_name="users")
    goods = models.ManyToManyField(Good, verbose_name="商品")

