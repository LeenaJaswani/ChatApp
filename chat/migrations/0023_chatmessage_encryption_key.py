# Generated by Django 5.0.1 on 2024-01-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0022_remove_chatmessage_body_chatmessage_encrypted_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='encryption_key',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
