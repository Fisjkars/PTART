# Generated by Django 2.2.1 on 2019-07-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0003_project_conclusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
