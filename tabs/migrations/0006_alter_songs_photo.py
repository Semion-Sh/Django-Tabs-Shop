# Generated by Django 4.1 on 2022-10-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0005_rename_tab_guitar_tabs_tab_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
