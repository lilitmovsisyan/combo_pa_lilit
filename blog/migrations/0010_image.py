# Generated by Django 2.1.1 on 2018-10-22 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_entry_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(default='', max_length=100)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Entry')),
            ],
        ),
    ]