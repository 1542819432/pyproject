from rest_framework import serializers
from .models import *


class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少2个字"
    })

    def create(self, validated_data):
        print("重写创建方法", validated_data)
        instance = Section.objects.create(**validated_data)
        print("创建模型实例", instance)
        return instance

    def update(self, instance, validated_data):
        print("重写更新方法", validated_data, instance.name)
        instance.name = validated_data.get("name", instance.name)
        print(instance.name)
        instance.save()
        return instance


class StaffSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=1, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少1个字"
    })

    section = SectionSerializer(label="分类")

    def validate_section(self, section):

        print("section原始值为", section)
        try:
            Section.objects.get(name=section["name"])
        except:
            raise serializers.ValidationError("输入的部门名不存在")

        return section

    def validate(self, attrs):
        print("收到的数据为", attrs)
        try:
            s = Section.objects.get(name=attrs["section"]["name"])
        except:
            s = Section.objects.create(name=attrs["section"]["name"])
        attrs["section"] = s
        print("更改之后的数据", attrs)
        return attrs

    def create(self, validated_data):
        print("创建staff参数", validated_data)
        instance = Staff.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.section)
        instance.name = validated_data.get("name", instance.name)
        instance.section = validated_data.get("section", instance.section)
        instance.save()
        return instance
