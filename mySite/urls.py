from django.urls import path

from members import views
from .views import (
    HomeView,
    ArticleDetailView,
    AddingPostView,
    UpdatingPostView,
    DeletingPostView,
    AddingCategoryView,
    CategoryView,
    category_list,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="post-details"),
    path("adding_posts/", AddingPostView.as_view(), name="adding_posts"),
    path("adding_categories/", AddingCategoryView.as_view(), name="adding_categories"),
    path("article/edit/<int:pk>", UpdatingPostView.as_view(), name="updating_posts"),
    path("article/<int:pk>/remove", DeletingPostView.as_view(), name="deleting_posts"),
    path("category/<str:categories>/", CategoryView, name="category"),
    path("category_list/", category_list, name="category_list"),
]
