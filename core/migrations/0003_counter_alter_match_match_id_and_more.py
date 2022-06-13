# Generated by Django 4.0.2 on 2022-04-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pricingplan_is_big_plan_alter_match_match_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_user', models.IntegerField(verbose_name='User number')),
                ('winning_matches', models.IntegerField(verbose_name='Winning matches')),
                ('people_love', models.IntegerField(verbose_name='People love')),
                ('is_active', models.BooleanField(default=True, verbose_name='Design if the Match is available')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default='48736827', unique=True, verbose_name='Match Id'),
        ),
        migrations.AlterField(
            model_name='pricingplan',
            name='is_big_plan',
            field=models.BooleanField(default=False, verbose_name='Design if the plan is Big'),
        ),
    ]
