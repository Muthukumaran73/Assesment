from django.db import models

class Distributor(models.Model):
    name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15)
    pan_number = models.CharField(max_length=10)
    bank_account_number = models.CharField(max_length=20)
    bank_ifsc = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)