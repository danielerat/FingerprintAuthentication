# Generated by Django 4.1.4 on 2023-01-07 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_hospital_healthfaculty_and_more'),
        ('patients', '0003_processing'),
    ]

    operations = [
        migrations.AddField(
            model_name='processing',
            name='HealthFaculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.healthfaculty'),
        ),
    ]
