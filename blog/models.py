from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    intro=models.TextField(null=True, blank=True)
    body=RichTextField(null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.slug==None:
            slug=slugify(self.title)

            has_slug=Post.objects.filter(slug=slug).exists()
            count=1
            while has_slug:
                count += 1
                slug=slugify(self.title) + '-' +str(count)
                has_slug=Post.objects.filter(slug=slug).exists()

            self.slug=slug

        super().save(*args, **kwargs)    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

