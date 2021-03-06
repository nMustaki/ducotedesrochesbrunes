# Generated by Django 3.2 on 2021-04-10 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(unique=True, verbose_name='date published')),
                ('max_seats', models.IntegerField(default=30)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrator.timeslot')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'time')},
            },
        ),
    ]
