# Generated by Django 5.0.1 on 2024-01-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0032_alter_chatmessage_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='ebody',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='key',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]