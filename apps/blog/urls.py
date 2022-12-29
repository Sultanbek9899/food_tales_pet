from django.urls import path

from apps.blog import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('products/', views.ProductsView.as_view(), name="products"),
    path('category/list/',views.CategoryListView.as_view(), name="category_list"),

    path('post/list/', views.PostListView.as_view(), name="post_list"),
    path(
        'post/list/<slug:category_slug>/', 
        views.PostListView.as_view(),
        name="post_category_list"
         ),

    path('post/detail/<int:pk>/',views.PostDetailView.as_view(), name="post_detail"),
]