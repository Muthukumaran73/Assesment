from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistributorViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'distributors', DistributorViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]