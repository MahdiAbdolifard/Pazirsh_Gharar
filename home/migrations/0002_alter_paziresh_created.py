# Generated by Django 4.2.2 on 2023-06-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paziresh',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]