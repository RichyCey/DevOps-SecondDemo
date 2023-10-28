# Generated by Django 4.1.7 on 2023-09-07 12:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимум 250 сим.', max_length=250, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публікації')),
                ('slug', models.SlugField(unique_for_date='pub_date', verbose_name='Слаг')),
                ('main_page', models.BooleanField(default=False, help_text='Показувати', verbose_name='Головна')),
            ],
            options={
                'verbose_name': 'Публікація',
                'verbose_name_plural': 'Публікації',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text='Максимум 250 символів', max_length=250, verbose_name='Категорія')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категорія для публікації',
                'verbose_name_plural': 'Категорії для публікацій',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Фото')),
                ('title', models.CharField(blank=True, help_text='Максимум 250 сим.', max_length=250, verbose_name='Заголовок')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='first_demo.article', verbose_name='Стаття')),
            ],
            options={
                'verbose_name': 'Фото для статті',
                'verbose_name_plural': 'Фото для статті',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='first_demo.category', verbose_name='Категорія'),
        ),
    ]
