from rest_framework import serializers
from ..models import Sale


class Sales:
    def __init__(self, sales):
        self.sales = sales
        


class SalesSerializer(serializers.Serializer):
    sales = serializers.ListField()




class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'title', 'descryption', 'image']