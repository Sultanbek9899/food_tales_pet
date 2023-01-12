from django import forms

from .models import Post, Comment

from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'image',
            'category',
            'tags',
            'is_draft',
        )
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control itrun"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "tags": forms.SelectMultiple(attrs={"class":"form-control"}),
            "is_draft":forms.CheckboxInput(attrs={"class":"form-control"})
        }

# forms.Form - Создаетформу, но не может сохранять данные в базу напрямую
# forms.ModelForm  - # Имеет связь с моделью и может сохранять данные в базу напрямую
class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text",]
        widgets = {
            "text":forms.Textarea(attrs={"class":"form-control"})
        }