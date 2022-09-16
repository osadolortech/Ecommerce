
from rest_framework import serializers
from .models import Product,Category,Chart



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
