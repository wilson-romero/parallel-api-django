from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'code', 'slug', 'name', 'description', 'is_published', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']



class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','code', 'slug', 'name', 'is_published', 'is_active', 'updated_at']
        read_only_fields = read_only_fields = read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
        