# Generated by Django 3.2.7 on 2021-11-08 16:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20211108_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serving',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Daily_intake',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_calories', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('maintain', 'maintain'), ('mild', 'mild'), ('lose', 'lose'), ('overlose', 'overlose'), ('exceed', 'exceed')], max_length=255, verbose_name='title')),
                ('recipe', models.ManyToManyField(to='food.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
