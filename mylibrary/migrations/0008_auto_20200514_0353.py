# Generated by Django 2.0.4 on 2020-05-14 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0007_card_bounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='bno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Borrow', to='mylibrary.Book'),
        ),
    ]
