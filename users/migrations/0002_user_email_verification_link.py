# Generated by Django 3.2.7 on 2024-12-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verification_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
