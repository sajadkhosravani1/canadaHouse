# Generated by Django 3.1.1 on 2020-09-05 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gopal', '0002_auto_20200905_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='media',
        ),
        migrations.AddField(
            model_name='media',
            name='house',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gopal.house'),
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='media',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
