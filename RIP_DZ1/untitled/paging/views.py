from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from products.models import Product

# Create your views here.


def get(request):
    return render(request,'Paging.html')


class BlogList(ListView):
    model = Product
    template_name = 'Paging.html'
    paginate_by = 9
    queryset = Product.objects.all()
