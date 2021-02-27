"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/21/21
"""
# coding: utf-8
from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
