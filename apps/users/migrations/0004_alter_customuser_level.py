# Generated by Django 5.0.3 on 2024-03-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_avatar_alter_customuser_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.SmallIntegerField(choices=[(0, 'Intern'), (1, 'Junior'), (2, 'Strong Junior'), (3, 'Middle'), (4, 'Strong Middle'), (5, 'Senior')], null=True),
        ),
    ]
