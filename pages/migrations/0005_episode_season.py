# Generated by Django 2.2.3 on 2019-07-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.IntegerField(default=1),
        ),
    ]
