# Generated by Django 5.0.3 on 2024-03-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='questionType',
            field=models.BooleanField(default=False, verbose_name='Question-Type'),
        ),
    ]