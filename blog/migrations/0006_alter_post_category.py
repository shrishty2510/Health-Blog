# Generated by Django 3.2.7 on 2022-03-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Mental Health', 'Mental Health'), ('Covid-19', 'Covid-19'), ('Heart Disease', 'Heart Disease'), ('Immune System', 'Immune System')], max_length=100),
        ),
    ]
