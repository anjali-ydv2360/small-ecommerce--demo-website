from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price_cents = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (${self.price_cents/100:.2f})"


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("canceled", "Canceled"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    total_cents = models.PositiveIntegerField(default=0)

    stripe_session_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status} - ${self.total_cents/100:.2f}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    price_cents = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"