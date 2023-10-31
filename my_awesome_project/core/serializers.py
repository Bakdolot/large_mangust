from rest_framework import serializers


class TestCreateSerializer(serializers.Serializer):
    deals = serializers.FileField()


class TestListSerializer(serializers.Serializer):
    username = serializers.CharField()
    spent_money = serializers.FloatField()
    gems = serializers.ListField(child=serializers.CharField())
