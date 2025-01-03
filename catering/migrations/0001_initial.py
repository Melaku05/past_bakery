# Generated by Django 5.0.1 on 2024-07-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('number_of_person', models.IntegerField(max_length=10)),
                ('date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
