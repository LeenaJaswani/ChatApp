# Generated by Django 5.0.1 on 2024-01-12 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0052_remove_chatmessage_body_chatmessage_ebody'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='ebody',
            new_name='body',
        ),
    ]