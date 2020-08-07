# Generated by Django 3.1 on 2020-08-07 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('img', models.URLField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('data_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
    ]
