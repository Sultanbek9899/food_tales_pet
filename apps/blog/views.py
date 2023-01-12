from wsgiref.util import request_uri
from django.shortcuts import render

from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    FormView,
    UpdateView,
)

from apps.blog.models import Category, Post, Comment
from apps.blog.forms import CommentCreateForm
# Create your views here.

# CBV - CLass Based Views - Вьюшки на классах
class IndexPage(TemplateView):
    template_name = "index.html"

# Function Based Views - Вьюшки основанные на функциях
# def index_page(request):
#     return render(request,"index.html")


class ProductsView(TemplateView):
        template_name = "products.html"



class CategoryListView(ListView):
    template_name = "category_list.html"
    model = Category
    queryset = Category.objects.all()


def get_categories(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request, 'category_list.html', context)


class PostListView(ListView):
    template_name ="post_list.html"
    model = Post
    queryset = Post.objects.filter(is_draft=False)

    # Отправка данных в шаблон через данный метод
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context
    
    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            qs = Post.objects.filter(is_draft=False, category__slug=category_slug)
            return qs
        return Post.objects.filter(is_draft=False)



class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post
    # pk=id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()
        context["comment_form"] = CommentCreateForm()

        return context

# Как бы выглядела логика , если бы писали на функциях 
# def get_detail_post(request,pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         pass
#     context = {
#         "post":post
#     }
#     return render(request, 'post_detail.html', context=context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostCreateForm

class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    template_name = "post_create.html"


    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)



class AuthorPostsListView(LoginRequiredMixin, ListView):
    template_name = "author_posts.html"
    model = Post


    def get_queryset(self):
        qs = Post.objects.filter(author=self.request.user)  
        return qs

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context


# def get_author_posts(request):
#     qs = Post.objects.filter(author=request.user)
#     context = {
#         "posts":qs
#     }
#     return render(request, 'author_posts.html', context)


from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

def delete_author_post(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404 
    post = get_object_or_404(Post, id=pk) 
    post.delete()
    return redirect(reverse_lazy("author_posts"))


def deactivate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk) 
    post.is_draft = True
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))


def activate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk) 
    post.is_draft = False
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))



class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostCreateForm
    model = Post
    success_url = reverse_lazy("author_posts")
    template_name = "post_create.html"


# Создать функцию обновления поста для примера.

# def update_post(request, pk):
#     post = get_object_or_404(Post,id=pk)

#     if request.method == "GET": # На получение данных
#         form = PostCreateForm(instance=post)
#         context = {
#             "form":form
#         }
#         return render(request, 'post_create.html', context)

#     elif request.method == "POST": # При отправке данных из формы.
#         form = PostCreateForm(
#             request.POST, 
#             request.FILES,
#             instance=post
#             )
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy("author_posts"))
#         context = {
#             "form":form
#         }
#         return render(request, 'post_create.html', context)




class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentCreateForm
    model = Comment

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk":self.kwargs.get("post_id")})
