# Generated by Django 2.2.3 on 2019-07-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190730_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='picture',
            field=models.ImageField(upload_to='static/images/hosts/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='profile',
            field=models.ImageField(upload_to='static/images/karly/%Y/%m/%d'),
        ),
    ]
