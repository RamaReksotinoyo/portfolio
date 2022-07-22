from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

# Create your models here.

class Category(models.Model):
    types = models.CharField(max_length=20)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.types

class Post(models.Model):
    title = models.CharField(max_length=100)
    intro=models.TextField(null=True, blank=True)
    body=RichTextField(null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)

    def image_tag(self):
        # return u'<img src="%s" />'  #escape(<URL to the image>)
        return mark_safe('<img src="{}" width=100 />'.format(self.image.url))
    image_tag.short_description = 'image'
    image_tag.allow_tags = True

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

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




