
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic  import DetailView
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, used previously as default forms
from django.contrib.auth.forms import PasswordChangeForm

from theblog.models import Profile
from .forms import SingUpForm,EditProfileForm, PasswordChangingForm  
from django.contrib.auth.views import PasswordChangeView


class UserRegistrationView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user = Profile.objects.all()
        context = super(ShowProfileView,self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self,):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm //former
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html')


        




