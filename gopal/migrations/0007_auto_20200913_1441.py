# Generated by Django 3.1.1 on 2020-09-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gopal', '0006_auto_20200906_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='public_remarks',
            field=models.TextField(null=True),
        ),
    ]
