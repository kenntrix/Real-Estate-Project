# plots/models.py
from django.db import models

class Plot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.PositiveIntegerField()
    image = models.ImageField(upload_to='plots/')
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('sold', 'Sold')])
    created_at = models.DateTimeField(auto_now_add=True)
 