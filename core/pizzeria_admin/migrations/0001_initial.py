# Generated by Django 4.2 on 2023-06-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsBookeeping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_data', models.BigIntegerField()),
                ('weekly_data', models.BigIntegerField()),
                ('monthly_data', models.BigIntegerField()),
                ('yearly_data', models.BigIntegerField()),
            ],
        ),
    ]
