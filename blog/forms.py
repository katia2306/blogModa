from django import forms

from .models import Post, Contacto, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image','text','tipo')

class ContactForm(forms.ModelForm):

        class Meta:
            model = Contacto
            fields = ('nombre', 'email', 'comment',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)