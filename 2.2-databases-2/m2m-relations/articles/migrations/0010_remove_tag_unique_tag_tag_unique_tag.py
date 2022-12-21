# Generated by Django 4.1.4 on 2022-12-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_title_tag_name_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='unique_tag',
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_tag'),
        ),
    ]