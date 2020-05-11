# Generated by Django 3.0.6 on 2020-05-11 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=125)),
                ('texto', models.TextField()),
                ('slug', models.SlugField()),
                ('data', models.DateField(auto_now=True)),
                ('postar', models.BooleanField(default=False)),
                ('curtidas', models.IntegerField()),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Sessao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(editable=False, max_length=125)),
                ('texto', models.TextField(editable=False, max_length=255)),
                ('avaliacao', models.IntegerField(editable=False)),
                ('aprovado', models.BooleanField(default=False)),
                ('data', models.DateField(auto_now=True)),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Postagem')),
            ],
        ),
    ]