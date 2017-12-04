# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('resumen', models.CharField(default='', max_length=400)),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Copia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventario', models.IntegerField(default=0)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_devolucion', models.DateTimeField()),
                ('copia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Copia')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('resumen', models.CharField(default='', max_length=400)),
                ('fecha_de_ingreso', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_comienzo', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.BooleanField(default=False)),
                ('copia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Copia')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Socio'),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Socio'),
        ),
        migrations.AddField(
            model_name='copia',
            name='ISBN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Libro'),
        ),
        migrations.AddField(
            model_name='autor',
            name='libros_publicados',
            field=models.ManyToManyField(to='biblio.Libro'),
        ),
    ]
