# Generated by Django 3.2.7 on 2022-03-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220315_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]