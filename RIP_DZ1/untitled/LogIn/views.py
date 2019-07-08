from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm, authenticate
from django.contrib.auth import login
from django.views import View
from django.views.generic import UpdateView
from .models import Profile as p
from .forms import Profile as ProfileForm
from django.contrib.auth.views import LoginView

# Create your views here.


class loginClass(LoginView):

    def get(self,request):
        form1 = AuthenticationForm
        return render(request,'Login.html',{'form': form1})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('log')
        # if user is not None:
        #     login(request,user)
        #     return redirect('index')
        # else:
        #     # the authentication system was unable to verify the username and password
        #     print("The username and password were incorrect.")


########################################################


class loginProfile(UpdateView):
    model = p
    template_name = 'Profile.html'
    form_class = ProfileForm

    def get_form(self, form_class=None):
        form = super(loginProfile,self).get_form()
        return form

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.filter(user=self.request.user).get()
        except:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['about'] = p.objects.get(user =self.request.user).about
            context['avatar'] = p.objects.get(user =self.request.user).avatar
        except:
            context['about'] = ''
            context['avatar'] = ''
        return context

    def get_success_url(self):
        return reverse('profile')


#index redirect
def indexRedirect(request):
    return redirect('index')
