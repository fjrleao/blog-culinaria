# Generated by Django 3.0.6 on 2020-05-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200511_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='curtidas',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='sessao',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]