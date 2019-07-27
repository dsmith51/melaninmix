# Generated by Django 2.2.3 on 2019-07-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='static/hosts/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=75)),
                ('text', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Amber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='static/amber/%Y/%m/%d')),
                ('bio', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField()),
                ('information', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='static/main/%Y/%m/%d')),
                ('blurb', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Karly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='static/karly/%Y/%m/%d')),
                ('bio', models.TextField(max_length=10000)),
            ],
        ),
    ]
