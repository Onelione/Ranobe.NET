# Generated by Django 2.2.7 on 2020-01-07 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191219_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chaptercomment',
            name='title',
        ),
    ]
