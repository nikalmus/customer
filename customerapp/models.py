from django.db import models
from .constants import STATE_CHOICES

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=10,null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='CO')

    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.city}, {self.state}"

