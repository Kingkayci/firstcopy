# Generated by Django 5.0 on 2024-01-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_rename_dashboard_mainwallet_accountbalance_dashboard_main_wallet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbalance',
            name='dash_all_transactions',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=10),
        ),
    ]
