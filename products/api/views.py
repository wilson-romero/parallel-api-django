from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from products.api.serializers import ProductListSerializer, ProductSerializer
from products.models import Product


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()

    lookup_field = 'slug'

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['code', 'name', 'description']
    ordering_fields = ['code', 'name', 'created_at', 'updated_at']
    ordering = ['code']

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer
    