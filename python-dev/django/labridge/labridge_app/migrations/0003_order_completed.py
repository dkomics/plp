# Generated by Django 5.0.3 on 2024-06-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labridge_app', '0002_remove_supplier_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
