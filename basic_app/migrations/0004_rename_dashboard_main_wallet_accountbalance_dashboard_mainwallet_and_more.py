# Generated by Django 5.0 on 2024-01-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountbalance',
            old_name='dashboard_main_wallet',
            new_name='dashboard_mainwallet',
        ),
        migrations.RenameField(
            model_name='accountbalance',
            old_name='dashboard_profit_wallet',
            new_name='dashboard_profitwallet',
        ),
        migrations.RenameField(
            model_name='accountbalance',
            old_name='deposit_main_wallet',
            new_name='deposit_mainwallet',
        ),
        migrations.RenameField(
            model_name='accountbalance',
            old_name='deposit_profit_wallet',
            new_name='deposit_profitwallet',
        ),
    ]
