# Generated by Django 4.2.2 on 2023-06-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_paziresh_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paziresh',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
