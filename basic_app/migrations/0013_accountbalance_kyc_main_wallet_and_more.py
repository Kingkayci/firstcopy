# Generated by Django 5.0 on 2024-01-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0012_uploadedreceipt_uploadkyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='kyc_main_wallet',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='kyc_profit_wallet',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='verify_kyc_main_wallet',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='verify_kyc_profit_wallet',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='verify_receipt_main_wallet',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='verify_receipt_profit_wallet',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=10),
        ),
    ]