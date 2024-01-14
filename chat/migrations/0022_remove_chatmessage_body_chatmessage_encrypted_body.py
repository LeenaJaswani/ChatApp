# Generated by Django 5.0.1 on 2024-01-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0021_remove_chatmessage_encryption_iv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='body',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='encrypted_body',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]