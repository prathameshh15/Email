# Generated by Django 4.2.5 on 2023-10-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_remove_members_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='otp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
