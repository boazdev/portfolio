# Generated by Django 5.1.4 on 2025-03-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(default='www.website.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=100),
        ),
    ]
