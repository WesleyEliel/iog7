# Generated by Django 4.0.6 on 2022-07-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_match_match_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default='52200771', unique=True, verbose_name='Match Id'),
        ),
    ]
