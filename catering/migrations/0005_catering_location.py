# Generated by Django 5.0.1 on 2024-07-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0004_alter_catering_catering_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='catering',
            name='location',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
    ]
