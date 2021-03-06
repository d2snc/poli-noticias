# Generated by Django 3.2.9 on 2021-12-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=400)),
                ('conteudo', models.CharField(max_length=2000)),
                ('data', models.DateTimeField()),
                ('tag', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=120)),
            ],
        ),
    ]
