from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView
                                  )

from .forms import ArticleModelForm
from .models import Article


class ArticleListView(ListView):
    # override the template
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # by default: <app_name>/<model_name>_list.html


class ArticleDetailView(DetailView):
    # override the template
    template_name = 'articles/article_detail.html'

    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        article_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=article_id)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self, queryset=None):
        article_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=article_id)

    def get_success_url(self):
        return reverse('articles:article-list')


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        article_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=article_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
