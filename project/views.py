# Create your views here.
from django.shortcuts import render_to_response, render
from django_tables2.config import RequestConfig
from project.models import ProductFilter, Product, ProductTable

def product_list(request):
    #f = ProductFilter(request.GET, queryset=Product.objects.all())
    config = RequestConfig(request)
    f = ProductTable(Product.objects.all(), prefix="1-")
    config.configure(f)
    return render(request, 'project/query.html', {'table': f})

def product_t(request):
    return render(request, 'project/query1.html', {})