# Generated by Django 2.1.1 on 2018-10-31 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20181006_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
