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

    path('post/create/', views.PostCreateView.as_view(), name="post_create"),
    path('post/author/list/', views.AuthorPostsListView.as_view(), name="author_posts"),
    path('post/delete/<int:pk>/', views.delete_author_post, name="post_delete"),
    path('post/deactivate/<int:pk>/', views.deactivate_author_post, name="deactivate_post"),
    path('post/activate/<int:pk>/', views.activate_author_post, name="activate_post"),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name="update_post"),

    path('comment/create/<int:post_id>/', views.CommentCreateView.as_view(), name="create_comment"),
]