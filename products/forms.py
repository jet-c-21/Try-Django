"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/18/21
"""
# coding: utf-8
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
