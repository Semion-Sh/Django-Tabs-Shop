# Generated by Django 4.1 on 2022-10-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0014_alter_guitar_tabs_tab_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_id', models.CharField(max_length=500)),
                ('users_email', models.CharField(max_length=500)),
                ('users_password', models.CharField(max_length=500)),
            ],
        ),
    ]
