# Generated by Django 4.1.4 on 2022-12-09 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_scope_only_one_main_tag_for_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes1', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
