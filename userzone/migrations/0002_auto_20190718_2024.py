# Generated by Django 2.2.3 on 2019-07-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='emailaddress',
            field=models.EmailField(max_length=50),
        ),
    ]
