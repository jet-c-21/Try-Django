"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/27/21
"""
# coding: utf-8
from django.urls import path
from .views import (my_fbv,
                    CourseView,
                    CourseListView,
                    CourseCreateView,
                    CourseUpdateView,
                    CourseDeleteView
                    )

app_name = 'courses'

urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    path('', CourseListView.as_view(), name='courses-list'),
    path('<int:course_id>/', CourseView.as_view(), name='courses-detail'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:course_id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:course_id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]
