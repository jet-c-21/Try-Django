from django.db import models
from django.urls import reverse


class Product(models.Model):
    # max_length arg is required for CharField
    title = models.CharField(max_length=120)

    '''
    blank is for ui render, null is for db
    but they should be in the same val (?)
    '''
    description = models.TextField(blank=True, null=True)

    # max_digits and decimal_places are required for DecimalField
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    summary = models.TextField(blank=True, null=True)

    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.title}"

    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        # use reverse to replace the hard code string (products)
        return reverse('products:product-detail', kwargs={'product_id': self.id})
