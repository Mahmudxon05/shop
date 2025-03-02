from django_filters import rest_framework as filters
from shop.models import *


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = "__all__"