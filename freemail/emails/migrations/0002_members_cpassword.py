# Generated by Django 4.2.5 on 2023-10-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='cpassword',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
