# Generated by Django 5.0.2 on 2024-02-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='static/media'),
        ),
    ]
