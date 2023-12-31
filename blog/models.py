from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.template.defaultfilters import slugify  # new
# Create your models here.

from django.utils.translation import gettext_lazy


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "comments/{filename}".format(filename=filename)


class Category(models.Model):
    categoryOptions = (
        ('hot', 'hot'),
        ('best', 'best'),
        ('new', 'new')
    )
    name = models.CharField(max_length=100, unique=True,
                            choices=categoryOptions)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Возвращать только опубликованные посты
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    options = (
        ("draft", "Draft"),  # draft - черновик
        ('published', "Published")
    )
    # on_delete=models.PROTECT при удалении категории пост не удаляется
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, to_field="name")
    title = models.TextField(max_length=300)
    image = models.ImageField(
        gettext_lazy("Image"), upload_to=upload_to, default='posts/default.jpg', null=True)
    # excerpt отрывок, null=True может быть пустым
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # Слаг нужен для того, чтобы генерировать удобные адреса страниц на сайте.
    slug = models.SlugField(max_length=300, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    # Поле related_name позволяет определить, как называть обратную ссылку.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default="published")
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        # Порядок в зависимости от даты добавления
        ordering = ("-published",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    image = models.ImageField(
        gettext_lazy("Image"), upload_to=user_directory_path, null=True)

    class Meta:
        ordering = ['created']
