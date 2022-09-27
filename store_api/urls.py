from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductView,CategoryView,ChartView,CheckoutView

router = DefaultRouter()
router.register("product", ProductView)
router.register("category", CategoryView)
router.register("chart",ChartView)
router.register("checkout", CheckoutView)

urlpatterns = [
    path("",include(router.urls))
]