# Generated by Django 5.0 on 2024-01-11 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0013_accountbalance_kyc_main_wallet_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountbalance',
            old_name='dash_deposit_bonus',
            new_name='dash_signup_bonus',
        ),
    ]