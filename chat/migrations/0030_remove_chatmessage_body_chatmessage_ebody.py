# Generated by Django 5.0.1 on 2024-01-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0029_remove_chatmessage_ebody_chatmessage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='body',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='ebody',
            field=models.BinaryField(blank=True),
        ),
    ]
