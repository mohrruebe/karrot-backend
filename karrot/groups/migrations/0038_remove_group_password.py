# Generated by Django 2.2.1 on 2019-05-20 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0037_group_welcome_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='password',
        ),
    ]
