from django.db import models
from django.utils import timezone

class Post(models.Model):
        TIPO = [
            ('Trendy', 'trendy'),
            ('Tips', 'tips'),
        ]
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to = 'images')
        tipo = models.CharField(max_length=20, choices=TIPO, default='trendy')
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Contacto(models.Model):
    author = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment

