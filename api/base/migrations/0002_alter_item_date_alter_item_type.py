# Generated by Django 4.0.5 on 2022-06-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('O', 'OFFER'), ('C', 'CATEGORY')], max_length=1),
        ),
    ]
