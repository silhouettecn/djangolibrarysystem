# Generated by Django 2.0.4 on 2018-05-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0004_auto_20180506_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]
