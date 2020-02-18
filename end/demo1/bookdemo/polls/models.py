from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    用户类继承原有的django用户类 方便
    """
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    # 一个问题可以被多个用户投票 关系字段需要写在多方
    titles = models.ManyToManyField('Title')


class Title(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Option(models.Model):
    choice = models.CharField(max_length=40)
    num = models.FloatField(default=0)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='option')

    def __str__(self):
        return self.choice
