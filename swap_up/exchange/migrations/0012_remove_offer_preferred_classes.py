# Generated by Django 3.1.2 on 2021-04-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0011_auto_20210413_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='preferred_classes',
        ),
    ]
