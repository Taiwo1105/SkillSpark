# Generated by Django 5.1.7 on 2025-03-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_course_enrollment_delete_placeholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to='course_materials/'),
        ),
    ]
