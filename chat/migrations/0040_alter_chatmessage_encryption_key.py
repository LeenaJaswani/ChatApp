# Generated by Django 5.0.1 on 2024-01-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0039_alter_chatmessage_encryption_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='encryption_key',
            field=models.BinaryField(default=b'1234'),
        ),
    ]