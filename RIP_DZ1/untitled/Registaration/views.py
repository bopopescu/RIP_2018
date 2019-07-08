from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from products.models import Product
# from LogIn.forms import ProfileForm
from .forms import RegistrationForm
from LogIn.models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
# Create your views here.


class Registration(View):
    def get(self,request):
        form = RegistrationForm
        return render(request, 'registration.html',{'form': form})

    def post(self,request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                my_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=my_password)
                login(request, user)
                # pObj = p.objects.create(user_id=self.kwargs['id'], about='', avatar='uploads/avatars/default.jpg')
                # p.save()
                return redirect('index')
        messages.info(request, 'Registration failed!')
        return redirect('Registration')


class Index(UserPassesTestMixin,ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 9
    queryset = Product.objects.all()
    ordering = ['id']

    def handle_no_permission(self):
        return redirect('log')

    def test_func(self):
        return self.request.user.is_authenticated



