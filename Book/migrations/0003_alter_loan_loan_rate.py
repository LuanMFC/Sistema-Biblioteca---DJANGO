# Generated by Django 5.0.2 on 2024-02-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_rate',
            field=models.FloatField(null=True),
        ),
    ]
