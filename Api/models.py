from django.db import models


# Create your models here.


class Pizza(models.Model):
    pizza_choices = (
        ("Regular", "Regular"),
        ("Square", "Square"),
    )
    pizza_choices_sizes = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large")
    )
    pizza_choices_toppings = (
        ("Onion", "Onion"),
        ("Tomato", "Tomato"),
        ("Corn", "Corn"),
        ("Capsicum", "Capsicum"),
        ("Cheese", "Cheese"),
        ("Jalapeno", "Jalapeno")
    )
    pizza_type = models.CharField(max_length=50, blank=True, null=True, choices=pizza_choices)
    pizza_size = models.CharField(max_length=50, blank=True, null=True, choices=pizza_choices_sizes)
    pizza_toppings = models.CharField(max_length=50, blank=True, null=True, choices=pizza_choices_toppings)

    def __str__(self):
        return self.pizza_type
