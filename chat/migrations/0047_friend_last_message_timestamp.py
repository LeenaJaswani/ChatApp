# Generated by Django 5.0.1 on 2024-01-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0046_remove_chatmessage_encryption_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='last_message_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
