# Generated by Django 4.1.6 on 2023-02-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_project_additional_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='additional_notes',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
