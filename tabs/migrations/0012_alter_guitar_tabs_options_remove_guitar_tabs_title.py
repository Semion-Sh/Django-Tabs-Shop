# Generated by Django 4.1 on 2022-10-05 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0011_remove_guitar_tabs_price_songs_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guitar_tabs',
            options={},
        ),
        migrations.RemoveField(
            model_name='guitar_tabs',
            name='title',
        ),
    ]
