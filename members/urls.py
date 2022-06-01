from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView, UserEditView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
