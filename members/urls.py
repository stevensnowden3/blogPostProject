from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView, UserEditView,PasswordsChangeView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/',views.password_success, name="password_success"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
