# Generated by Django 3.2.7 on 2022-03-15 09:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0005_auto_20220315_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(max_length=7)),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh (AR)', 'Arunachal Pradesh (AR)'), ('Assam (AS)', 'Assam (AS)'), ('Bihar (BR)', 'Bihar (BR)'), ('Chhattisgarh (CG)', 'Chhattisgarh (CG)'), ('Goa (GA)', 'Goa (GA)'), ('Gujarat (GJ)', 'Gujarat (GJ)'), ('Haryana (HR)', 'Haryana (HR)'), ('Himachal Pradesh (HP)', 'Himachal Pradesh (HP)'), ('Jammu and Kashmir (JK)', 'Jammu and Kashmir (JK)'), ('Jharkhand (JH)', 'Jharkhand (JH)'), ('Karnataka (KA)', 'Karnataka (KA)'), ('Kerala (KL)', 'Kerala (KL)'), ('Madhya Pradesh (MP)', 'Madhya Pradesh (MP)'), ('Maharashtra (MH)', 'Maharashtra (MH)'), ('Manipur (MN)', 'Manipur (MN)'), ('Meghalaya (ML)', 'Meghalaya (ML)'), ('Mizoram (MZ)', 'Mizoram (MZ)'), ('Nagaland (NL)', 'Nagaland (NL)'), ('Odisha(OR)', 'Odisha(OR)'), ('Punjab (PB)', 'Punjab (PB)'), ('Rajasthan (RJ)', 'Rajasthan (RJ)'), ('Sikkim (SK)', 'Sikkim (SK)'), ('Tamil Nadu (TN)', 'Tamil Nadu (TN)'), ('Telangana (TS)', 'Telangana (TS)'), ('Tripura (TR)', 'Tripura (TR)'), ('Uttar Pradesh (UP)', 'Uttar Pradesh (UP)'), ('Uttarakhand (UK)', 'Uttarakhand (UK)'), ('West Bengal (WB)', 'West Bengal (WB)')], max_length=30)),
                ('pin', models.CharField(max_length=30)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
