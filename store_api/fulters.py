from dataclasses import fields
from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            "category": ['exact'],"old_price": ['gt','lt'],"product_name":['exact']
        }