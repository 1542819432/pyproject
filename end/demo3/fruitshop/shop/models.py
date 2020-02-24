from django.db import models


# Create your models here.

class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name="图片")


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名")
    price = models.FloatField(verbose_name="价格")
    size = models.CharField(verbose_name="尺寸")
    matures = models.CharField(verbose_name="成熟期")
    explain = models.CharField(max_length=100, verbose_name="说明")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    body = models.CharField(max_length=500, verbose_name="评论内容")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="所属商品")

    def __str__(self):
        return self.name

