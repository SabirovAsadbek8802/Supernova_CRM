# Generated by Django 5.0.2 on 2024-03-03 04:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_boss', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.'), django.core.validators.RegexValidator(message='Enter a valid email address matching the format example@example.com', regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')])),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('skype', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('intern', 'Intern'), ('junior', 'Junior'), ('junior++', 'Junior++'), ('middle', 'Middle'), ('middle++', 'Middle++'), ('senior', 'Senior')], max_length=255)),
                ('avatar', models.ImageField(upload_to='../media/avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]