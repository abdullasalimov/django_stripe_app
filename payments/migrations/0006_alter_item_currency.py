# Generated by Django 4.1.1 on 2022-09-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('rub', 'rub')], default='usd', max_length=3),
        ),
    ]