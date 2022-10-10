
from calendar import c
from dataclasses import fields
from rest_framework import serializers
from .models import Product,Category,Chart,Checkout



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=[
            "id","title","category_image","description"
        ]


class ProductSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=[
            "id","product_name","product_iamge","category","old_price","price","inventory"
        ]

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = [
            "id","user","product"
        ]

class CheckoutSerializer(serializers.ModelSerializer):
    product_in_chart = ChartSerializer()
    class Meta:
        model = Checkout
        fields=[
            "id","user","product_in_chart","payment_on_delivery","card_payment"
        ]