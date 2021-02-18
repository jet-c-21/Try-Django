"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/18/21
"""
# coding: utf-8
from django import forms

from .models import Product


class ProductFormWithValidation(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your title'}))

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

    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'email',
        ]

    def clean_title(self, *args, **kwargs):
        """
        clean_xxx is a built-in name
        if you change clean to cleanx or clean_x_title, it will not work anymore!
        :param args:
        :param kwargs:
        :return:
        """
        title = self.cleaned_data.get('title')
        if 'puff' in title:
            return title
        else:
            raise forms.ValidationError('this is not a valid title')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('this is not a valid email')
        return email


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your title'}))

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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
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
