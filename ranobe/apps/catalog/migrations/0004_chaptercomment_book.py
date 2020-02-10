# Generated by Django 2.2.7 on 2020-01-08 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_chaptercomment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaptercomment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.Book', verbose_name='Книга'),
            preserve_default=False,
        ),
    ]