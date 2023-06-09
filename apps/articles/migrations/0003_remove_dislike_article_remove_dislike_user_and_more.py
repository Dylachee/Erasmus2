# Generated by Django 4.2.1 on 2023-05-06 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_comment_dislike_favorite_like_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislike',
            name='article',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='article',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='article',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DisLike',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
