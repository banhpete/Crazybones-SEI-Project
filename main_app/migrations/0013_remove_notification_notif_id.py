# Generated by Django 3.0.7 on 2020-07-09 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200709_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notif_id',
        ),
    ]
