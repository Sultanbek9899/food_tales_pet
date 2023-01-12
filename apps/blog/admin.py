from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

# Register your models here.
from apps.blog.models import Category, Post, Tag

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'




@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ["title", "category","created", "is_draft",]
    list_filter = ["category", "is_draft", "created"]
    filter_horizontal = ["tags"]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name", "slug","id"]

    