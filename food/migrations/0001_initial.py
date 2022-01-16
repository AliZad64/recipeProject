# Generated by Django 3.2.7 on 2021-11-08 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('measure', models.CharField(choices=[('gram', 'gram'), ('tbsp', 'tbsp'), ('cup', 'cup'), ('single', 'single')], max_length=255, verbose_name='title')),
                ('calories', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('note', models.CharField(default='', max_length=255)),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.ingredient')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('photo', models.ImageField(upload_to='recipes/')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('time_of_create', models.DateField(default=django.utils.timezone.now)),
                ('recipe_description', models.TextField(default='')),
                ('total_calories', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('total_carbs', models.IntegerField(blank=True, null=True)),
                ('recipe_ingredient', models.ManyToManyField(related_name='recipe', to='food.Item', verbose_name='items')),
                ('recipe_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.recipetype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingrident_species', to='food.species'),
        ),
    ]