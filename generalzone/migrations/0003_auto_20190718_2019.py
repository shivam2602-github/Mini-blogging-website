# Generated by Django 2.2.3 on 2019-07-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0002_customerinfo_logininfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='emailaddress',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
