
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, used previously as default forms
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SingUpForm,EditProfileForm
from django.contrib.auth.views import PasswordChangeView


class UserRegistrationView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self,):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html')


        




