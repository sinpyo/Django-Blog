from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ['cat_id', 'board_id', 'post_notice', 'post_name', 'post_content']

        widgets = {
            'cat_id': forms.Select(
                attrs={'class': 'custom-select'}
            ),

            'board_id': forms.Select(
                attrs={'class': 'custom-select'}
            ),

            'post_notice': forms.CheckboxInput(

            ),

            'post_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),

            'post_content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['cmt_content']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=CKEditorUploadingWidget(), required=True)
