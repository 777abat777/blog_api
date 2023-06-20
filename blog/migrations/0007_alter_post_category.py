# Generated by Django 4.2.1 on 2023-06-15 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_name_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(choices=[('hot', 'hot'), ('best', 'best'), ('new', 'new')], on_delete=django.db.models.deletion.PROTECT, to='blog.category', to_field='name'),
        ),
    ]