# Generated by Django 5.0 on 2024-01-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_alter_accountbalance_dash_rank_achieved'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='dash_amount',
            field=models.CharField(blank=True, default='+5 USD', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_amount1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_amount2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_amount3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_description1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_description2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_description3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_description_default',
            field=models.CharField(blank=True, default='signup bonus', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_fee',
            field=models.CharField(blank=True, default='0 USD', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_fee1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_fee2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_fee3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_gateway',
            field=models.CharField(blank=True, default='system', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_gateway1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_gateway2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_gateway3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_status',
            field=models.CharField(blank=True, default='success', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_status1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_status2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_status3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_transactionID1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_transactionID2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_transactionID3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_transactionID_default',
            field=models.CharField(blank=True, default='TRXYLNKPNUR5K', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_type',
            field=models.CharField(blank=True, default='signup bonus', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_type1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_type2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='dash_type3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_amount',
            field=models.CharField(blank=True, default='+5 USD', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_amount1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_amount2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_amount3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_amount4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_description1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_description2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_description3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_description4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_description_default',
            field=models.CharField(blank=True, default='signup bonus', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_fee',
            field=models.CharField(blank=True, default='0 USD', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_fee1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_fee2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_fee3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_fee4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_gateway',
            field=models.CharField(blank=True, default='system', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_gateway1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_gateway2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_gateway3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_gateway4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_status',
            field=models.CharField(blank=True, default='success', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_status1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_status2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_status3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_status4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_transactionID1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_transactionID2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_transactionID3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_transactionID4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_transactionID_default',
            field=models.CharField(blank=True, default='TRXYLNKPNUR5K', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_type',
            field=models.CharField(blank=True, default='signup bonus', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_type1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_type2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_type3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_type4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_amount',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_amount1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_amount2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_amount3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_amount4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_description1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_description2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_description3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_description4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_description_default',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_fee',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_fee1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_fee2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_fee3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_fee4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_gateway',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_gateway1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_gateway2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_gateway3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_gateway4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_status',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_status1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_status2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_status3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_status4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_transactionID1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_transactionID2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_transactionID3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_transactionID4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='withdraw_transactionID_default',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
