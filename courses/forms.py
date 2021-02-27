"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/27/21
"""
# coding: utf-8
from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]

    # def clean_<field_name>()
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'fuck':
            raise forms.ValidationError('This is not a valid title')
        return title

