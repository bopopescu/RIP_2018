from django.shortcuts import reverse
from django.views.generic import ListView, UpdateView, CreateView
from .models import Product
from .forms import ProdForm, ProdFormAddNew
from .mixins import GroupRequiredMixin


class ProductView(ListView):
    model = Product


class AddProduct(GroupRequiredMixin, UpdateView):
    model = Product
    template_name = 'profile_update.html'
    form_class = ProdForm
    group_required = [u'redactors'];

    def get_object(self):
        return Product.objects.get(pk=self.kwargs["id"])

    def get_success_url(self):
        id = self.kwargs['id']
        return reverse('profile_update', kwargs={'id': id})


class AddNewProduct(GroupRequiredMixin, CreateView):
    model = Product
    template_name = 'profile_add.html'
    form_class = ProdFormAddNew
    group_required = [u'redactors'];

    # def get_success_url(self):
    #     return reverse('profile_add')
    # для удобства добавления но не как в ТЗ

    def get_success_url(self):
        return reverse('profile_update',kwargs={'id': Product.objects.all().count()})
