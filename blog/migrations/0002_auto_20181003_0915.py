# Generated by Django 2.1.2 on 2018-10-03 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='last_update_time',
            new_name='last_updated_time',
        ),
    ]
