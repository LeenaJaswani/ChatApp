# Generated by Django 5.0.1 on 2024-01-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0030_remove_chatmessage_body_chatmessage_ebody'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='key',
            field=models.CharField(default='key', max_length=24),
        ),
    ]
