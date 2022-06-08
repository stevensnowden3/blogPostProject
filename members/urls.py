from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ShowProfileView, EditProfilePageView, CreateProfilePageView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile', ShowProfileView.as_view(), name="user_profile"),
    path('<int:pk>/edit_profile_page',
         EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile_page/', CreateProfilePageView.as_view(),
         name="create_user_profile_page"),

    path('passwordw/', views.password_su, name="password_su"),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
