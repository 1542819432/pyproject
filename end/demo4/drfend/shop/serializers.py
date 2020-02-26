from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category 的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在Meta类中 model指明序列化的模型 fields指明序列化的字段
    """

    # goods 要和related_name 的值一致

    # StringRelatedField() 可以显示关联数据模型中的__str__ 返回值   many=True 代表多个对象   read_only=True代表只读
    # goods =serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    goods = serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('name','goods')


class GoodSerializer(serializers.ModelSerializer):

    # 在序列化时指定字段 在多方 使用source = 模型名.字段名 read_only=True 表示只读
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name','desc','category')

