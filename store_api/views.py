from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProductSerilaizer,CategorySerializer,ChartSerializer,CheckoutSerializer
from .models import Product,Category,Chart,Checkout
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .fulters import ProductFilter
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser,FormParser]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['product_name','^product_name']
    ordering_fields = ['old_price']
    filterset_class = ProductFilter


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser,FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','^title']


class ChartView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CheckoutView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


    