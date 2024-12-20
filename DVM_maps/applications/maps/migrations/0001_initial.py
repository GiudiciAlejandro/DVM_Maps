# Generated by Django 4.1.7 on 2024-12-19 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('primary_srv', models.CharField(max_length=100, verbose_name='DVM primary server')),
                ('redundant_srv', models.CharField(blank=True, max_length=100, null=True, verbose_name='DVM redundant server')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.project')),
            ],
        ),
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('jump', models.CharField(max_length=255, verbose_name='Jump to page')),
                ('pox', models.IntegerField()),
                ('poy', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.site')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('number', models.IntegerField()),
                ('primary_srv', models.CharField(max_length=100, verbose_name='DVM primary server')),
                ('redundant_srv', models.CharField(blank=True, max_length=100, null=True, verbose_name='DVM redundant server')),
                ('pox', models.IntegerField()),
                ('poy', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.site')),
            ],
        ),
    ]
