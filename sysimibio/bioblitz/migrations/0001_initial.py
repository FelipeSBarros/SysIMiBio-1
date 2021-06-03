# Generated by Django 3.2 on 2021-05-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioblitzProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconURL', models.URLField(blank=True, verbose_name='URL del icono del proyecto')),
                ('description', models.TextField(blank=True, verbose_name='Descripción del proyecto')),
                ('created_at', models.DateTimeField(verbose_name='Fecha de creacción')),
                ('title', models.CharField(max_length=200, verbose_name='Título del proyecto')),
                ('project_id', models.IntegerField(unique=True, verbose_name='Id del proyecto')),
                ('project_slug', models.CharField(max_length=250, verbose_name='Slug del proyecto')),
                ('place_id', models.IntegerField(unique=True, verbose_name='Id del local')),
                ('project_type', models.CharField(max_length=100, verbose_name='Tipo de proyecto')),
                ('manager_id', models.IntegerField(unique=True, verbose_name='Id del administrador')),
                ('manager_login', models.CharField(max_length=200, verbose_name='Login del administrador')),
                ('manager_name', models.CharField(max_length=200, verbose_name='Nombre del administrador')),
            ],
        ),
    ]