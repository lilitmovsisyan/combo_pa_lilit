# Generated by Django 2.1.1 on 2018-10-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_entry_entry_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry_text',
            new_name='text',
        ),
    ]
