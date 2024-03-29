# Generated by Django 5.0 on 2024-01-09 12:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dashboard_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('deposit_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('deposit_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('deposit_logs_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('deposit_logs_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('ranking_badge_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('ranking_badge_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('referral_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('referral_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('schemas_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('schemas_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('schema_logs_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('schema_logs_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('transactions_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('transactions_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('withdraw_logs_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('withdraw_logs_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('withdraw_main_wallet', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('withdraw_profit_wallet', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('dash_all_transactions', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_deposit', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_investment', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_profit', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_transfer', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_withdraw', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_referral_bonus', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_deposit_bonus', models.DecimalField(decimal_places=1, default=5, max_digits=10)),
                ('dash_investment_bonus', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_referral', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_rank_achieved', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('dash_total_ticket', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
