# Generated by Django 3.2 on 2021-06-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioblitz', '0002_auto_20210603_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bioblitzoccurrence',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bioblitzoccurrence',
            name='rank',
        ),
        migrations.AddField(
            model_name='bioblitzoccurrence',
            name='taxon_name',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Nombre cientifico de la especie'),
        ),
        migrations.AddField(
            model_name='bioblitzoccurrence',
            name='taxon_rank',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Ranking taxonomico'),
        ),
        migrations.AlterField(
            model_name='bioblitzoccurrence',
            name='iconic_taxon_name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Ranking taxonomico'),
        ),
    ]