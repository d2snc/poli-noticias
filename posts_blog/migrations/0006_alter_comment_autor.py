# Generated by Django 3.2.9 on 2021-12-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_blog', '0005_alter_comment_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='autor',
            field=models.CharField(max_length=50),
        ),
    ]
