from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductView,CategoryView

router = DefaultRouter()
router.register("product", ProductView)
router.register("category", CategoryView)

urlpatterns = [
    path("",include(router.urls))
]