# Generated by Django 5.0.1 on 2024-01-12 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0059_chatmessage_ebody_alter_chatmessage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='ebody',
        ),
    ]