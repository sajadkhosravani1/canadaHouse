# Generated by Django 3.1.1 on 2020-09-05 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('src', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('public_remarks', models.TextField()),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('dateListed', models.DateTimeField()),
                ('mediaURL', models.TextField()),
                ('sizel', models.IntegerField()),
                ('sizeh', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('acres', models.FloatField()),
                ('title', models.TextField()),
                ('position_lat', models.IntegerField()),
                ('position_lng', models.IntegerField()),
                ('office', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gopal.city')),
                ('lol_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gopal.type')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gopal.media')),
                ('ownership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gopal.ownership')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gopal.state')),
            ],
        ),
    ]