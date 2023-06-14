from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.template.defaultfilters import slugify  # new
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    class PostObjects(models.Manager): #Возвращать только опубликованные посты
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    options=(
        ("draft","Draft"),#draft - черновик
        ('published',"Published")
    )
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)#on_delete=models.PROTECT при удалении категории пост не удаляется
    title =models.TextField(max_length=300)
    excerpt=models.TextField(null=True)#excerpt отрывок, null=True может быть пустым 
    content=models.TextField()
    slug=models.SlugField(max_length=300,unique_for_date='published')#Слаг нужен для того, чтобы генерировать удобные адреса страниц на сайте.
    published=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_posts')#Поле related_name позволяет определить, как называть обратную ссылку.
    status=models.CharField(max_length=10,choices=options,default="published")
    objects=models.Manager() #default manager
    postobjects=PostObjects() #custom manager
    class Meta:
        ordering=("-published",)#Порядок в зависимости от даты добавления
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)