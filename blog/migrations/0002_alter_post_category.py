# Generated by Django 3.2.7 on 2022-03-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Mental Health', 'Mental Health'), ('Covid-19', 'Covid-19'), ('Heart Disease', 'Heart Disease'), ('Immune system', 'Immune System')], max_length=100),
        ),
    ]
