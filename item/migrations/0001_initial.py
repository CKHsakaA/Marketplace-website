# Generated by Django 3.2.12 on 2024-02-17 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(null=True, upload_to='category_imagesScalae')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('manufacturer', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='item_images')),
                ('is_sold', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
