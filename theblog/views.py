from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from theblog.models import Category, Post
from .forms import PostForm

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-created_at']

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats':cats.title(), 'category_posts':category_posts})

class ArticlaDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields =  ('title', 'body')
    # fields =  '__all__'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields =  '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    



