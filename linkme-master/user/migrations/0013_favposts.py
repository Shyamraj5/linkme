# Generated by Django 4.2.3 on 2023-07-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_remove_posts_favp_posts_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favposts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav', models.ManyToManyField(related_name='favo', to='user.posts')),
            ],
        ),
    ]
