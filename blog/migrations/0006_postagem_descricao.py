# Generated by Django 3.0.6 on 2020-05-12 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200511_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='descricao',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
