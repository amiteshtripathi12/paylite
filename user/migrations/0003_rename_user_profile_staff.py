# Generated by Django 4.1.1 on 2022-12-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_account_profile_bank_profile_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='staff',
        ),
    ]