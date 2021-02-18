from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm


def render_initial_data(request):
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         print(title)
#
#     context = {
#     }
#     return render(request, 'products/product_create.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }

    context = {
        'object': obj
    }

    return render(request, 'products/product_detail.html', context)
