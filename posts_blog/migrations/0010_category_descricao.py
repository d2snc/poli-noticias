# Generated by Django 3.2.9 on 2021-12-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_blog', '0009_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descricao',
            field=models.CharField(max_length=400, null=True),
        ),
    ]