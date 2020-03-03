from rest_framework import serializers
from .models import *


class GoodSerializer1(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方 使用source = 模型名.字段名 read_only=True 表示只读
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('id', 'name', 'desc', 'category')


class CustomSerializer(serializers.ModelSerializer):
    """
    自定义序列化类
    """

    def to_representation(self, value):
        """
        重写字段的输出格式
        :param value: 需要序列化对象
        :return: 显示的格式
        """
        return str(value.id) + "--" + value.desc


class CategorySerializer(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少2个字"
    })

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

    category = CategorySerializer(label="分类")
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


class CategorySerializer1(serializers.ModelSerializer):
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
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)

    # 自定义序列化类
    goods = CustomSerializer(many=True, read_only=True)

    # goods = GoodSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('id', 'name', 'goods')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["user_permissions", "groups"]

    def validate(self, attrs):
        from django.contrib.auth import hashers
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        return attrs


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3, error_messages={
        'required': "用户名必填"
    })
    password = serializers.CharField(max_length=10, min_length=3, write_only=True)
    password2 = serializers.CharField(max_length=10, min_length=3, write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("密码不一致")
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get("username"), email=validated_data.get("email"),
                                        password=validated_data.get("password"))

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

