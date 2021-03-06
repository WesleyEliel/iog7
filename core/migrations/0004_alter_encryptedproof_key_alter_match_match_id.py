# Generated by Django 4.0.2 on 2022-04-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_counter_alter_match_match_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedproof',
            name='key',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default='49628541', unique=True, verbose_name='Match Id'),
        ),
    ]
