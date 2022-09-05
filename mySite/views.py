from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from .forms import PostForm, EditPostForm

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    category = Category.objects.all()
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class HomePage(ListView):
    model = Post
    template_name = "homepage.html"
    category = Category.objects.all()
    ordering = ["post_date"]

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def category_list(request):
    category_menu_list = Category.objects.all()
    context = {"category_menu_list": category_menu_list}
    return render(request, "../templates/registration/categories/category_list.html", context)


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace("-", " "))
    context = {
        "categories": categories.title().replace("-", " "),
        "category_posts": category_posts,
    }
    return render(request, "../templates/registration/categories/categories.html", context)


class ArticleDetailView(DetailView):
    model = Post
    template_name = "../templates/registration/posts_folder/post_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class AddingPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "../templates/registration/posts_folder/adding_posts.html"


class AddingCategoryView(CreateView):
    model = Category
    template_name = "../templates/registration/categories/adding_categories.html"
    fields = "__all__"
    # fields = ('title','author', 'body')


class UpdatingPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "../templates/registration/posts_folder/updating_posts.html"
    # fields = ['title','title_tag', 'body']


class DeletingPostView(DeleteView):
    model = Post
    template_name = "../templates/registration/posts_folder/deleting_posts.html"
    success_url = reverse_lazy("home")
