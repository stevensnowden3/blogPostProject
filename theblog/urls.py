from django.urls import include, path
from .views import AddPostView, CategoryView, HomeView, ArticlaDetailView, UpdatePostView, DeletePostView, AddCategoryView, LikeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name="home"), //for view not class view
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticlaDetailView.as_view(), name="article_details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),


    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>/', LikeView, name="like_post"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
