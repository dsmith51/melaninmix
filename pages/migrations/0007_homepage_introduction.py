# Generated by Django 2.2.3 on 2019-07-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_episode_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='introduction',
            field=models.TextField(default='testdata', max_length=20000),
            preserve_default=False,
        ),
    ]