# Generated by Django 5.0.1 on 2024-01-11 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0045_alter_chatmessage_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='encryption_key',
        ),
    ]