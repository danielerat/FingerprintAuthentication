# Generated by Django 4.1.4 on 2023-01-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_rename_healthfaculty_processing_healthfaculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='patriarch',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
