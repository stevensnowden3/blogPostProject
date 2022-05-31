from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationView

urlpatterns = [
    path('', UserRegistrationView.as_view(), name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
