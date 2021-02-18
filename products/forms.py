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


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'your title'
        }
    ))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'your description',
                                          'class': 'nice-text-area',
                                          'rows': 3,
                                          'cols': 30,
                                      }
                                  ))

    price = forms.DecimalField(initial=9.99)
