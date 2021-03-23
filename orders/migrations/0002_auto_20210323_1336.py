# Generated by Django 3.1.7 on 2021-03-23 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_profile', '0002_remove_useraddress_phone'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user_prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription',
                                    to='user_profile.prescription'),
        ),
    ]
