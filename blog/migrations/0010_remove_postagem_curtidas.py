# Generated by Django 3.0.6 on 2020-05-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200512_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='curtidas',
        ),
    ]
