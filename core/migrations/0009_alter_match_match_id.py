# Generated by Django 4.0.5 on 2022-06-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_match_match_id_alter_match_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default='24243407', unique=True, verbose_name='Match Id'),
        ),
    ]
