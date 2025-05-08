from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Distributor, Payment
from .serializers import DistributorSerializer, PaymentSerializer
from .integrations.cashfree import confirm_payment_with_cashfree

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        transaction_id = request.data.get("transaction_id")
        is_valid = confirm_payment_with_cashfree(transaction_id)
        if not is_valid:
            return Response({"error": "Payment not confirmed"}, status=400)
        return super().create(request, *args, **kwargs)