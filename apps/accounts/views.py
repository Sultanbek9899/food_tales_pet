from django.shortcuts import render, redirect

from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

from apps.accounts.forms import LoginForm, UserRegisterForm
from apps.accounts.models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name ="login.html"

    def form_valid(self, form):
        data = form.cleaned_data #{"password":"admin", "email":"admin@gmail.com"}
        # cleaned_data хранилище данных из формы в виде dict
        print(data)
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email,password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("Ваш аккаунт не активен!")
        return HttpResponse("Введенные вами данные некорректные!")



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")

from django.http import HttpResponseRedirect
from apps.accounts.utils import send_activation_email
class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('register_done')


    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_activation_email(user,request=self.request, to_email=user.email)
        return HttpResponseRedirect(self.get_success_url())



class RegisterDoneView(TemplateView):
    template_name = "register_done.html"