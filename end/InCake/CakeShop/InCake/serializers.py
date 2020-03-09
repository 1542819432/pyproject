from rest_framework import serializers
from .models import *


class GoodImgsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值", attrs["good"]["name"])
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
            print("修改商品", g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.img, instance.good)
        instance.img = validated_data.get("img", instance.img)
        instance.good = validated_data.get("good", instance.good)
        instance.save()
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=1, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少1个字"
    })

    imgs = GoodImgsSerializer(label="图片", many=True, read_only=True)

    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回新值
        """
        print("category原始值为", category)
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return category

    def validate(self, attrs):
        print("收到的数据为", attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        print("更改之后的数据", attrs)
        return attrs

    def create(self, validated_data):
        print("创建good参数", validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, min_length=1, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少1个字"
    })

    goods = GoodSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        通过创建create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print("重写创建方法", validated_data)
        instance = Category.objects.create(**validated_data)
        print("创建模型实例", instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update,来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回新实例
        """
        print("重写更新方法", validated_data, instance.name)
        instance.name = validated_data.get("name", instance.name)
        print(instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    password = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
