# Generated by Django 3.2.7 on 2021-11-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20211108_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_intake',
            name='intake_calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
