# Generated by Django 2.2.7 on 2019-12-13 17:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='Никнейм')),
            ],
            options={
                'verbose_name': 'Автор',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('summary', models.TextField(help_text='Краткое описание данной книги.', max_length=500, verbose_name='Описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('book_rating', models.IntegerField(default=0, verbose_name='Средняя оценка данной книги')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/books', verbose_name='Изображение книги')),
                ('last_pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации последней главы')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Author', verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Навзание')),
                ('price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('content', models.TextField(default='Содержание главы...', verbose_name='Содержание главы')),
                ('number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер главы')),
                ('status', models.CharField(choices=[('f', 'Бесплатный'), ('p', 'Платный')], default='f', help_text='Статус главы', max_length=1, verbose_name='Статус')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
                ('pay_users', models.ManyToManyField(blank=True, help_text='Пользователи, что купили данную главу', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название страны.', max_length=100, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название жанра.', max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Навзание рецензии')),
                ('content', models.TextField(verbose_name='Содержание рецензии')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('rating', models.IntegerField(help_text='Оценка пользователья к данной книге ( 1 - 5)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=100, verbose_name='Навзание кометария')),
                ('content', models.TextField(max_length=500, verbose_name='Содержание кометария')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Chapter', verbose_name='Глава')),
                ('commentator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Country'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Жанры данной книги.', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
