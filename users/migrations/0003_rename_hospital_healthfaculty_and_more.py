# Generated by Django 4.1.4 on 2023-01-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_hospital_remove_profile_bio_remove_profile_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hospital',
            new_name='HealthFaculty',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='hospital',
            new_name='HealthFaculty',
        ),
    ]
