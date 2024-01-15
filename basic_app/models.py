from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UploadedReceipt(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')

class UploadKYC(models.Model):
    card = models.ImageField(upload_to="profile_pics")
    imagePassport = models.ImageField(upload_to="profile_pics")

class ContactForm(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.CharField(max_length=900)



class AccountBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dashboard_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    deposit_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    deposit_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    deposit_logs_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    deposit_logs_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    ranking_badge_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    ranking_badge_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    referral_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    referral_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    schemas_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    schemas_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    schema_logs_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    schema_logs_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    transactions_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    transactions_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    withdraw_logs_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    withdraw_logs_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    withdraw_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    withdraw_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    kyc_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    kyc_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    verify_kyc_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    verify_kyc_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    verify_receipt_main_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    verify_receipt_profit_wallet = models.DecimalField(max_digits=10, decimal_places=1, default=5)



    dash_all_transactions = models.DecimalField(max_digits=10, decimal_places=1, default=1)
    dash_total_deposit = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_total_investment = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_total_profit = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_total_transfer = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_total_withdraw = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_referral_bonus = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_signup_bonus = models.DecimalField(max_digits=10, decimal_places=1, default=5)
    dash_investment_bonus = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_total_referral = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    dash_rank_achieved = models.DecimalField(max_digits=10, decimal_places=1, default=1)
    dash_total_ticket = models.DecimalField(max_digits=10, decimal_places=1, default=0)


    dash_description_default = models.CharField(max_length=20, blank=True, default="signup bonus")
    dash_transactionID_default = models.CharField(max_length=20, blank=True, default="TRXYLNKPNUR5K")
    dash_type = models.CharField(max_length=20, blank=True, default="signup bonus")
    dash_amount = models.CharField(max_length=20, blank=True, default="+5 USD")
    dash_fee = models.CharField(max_length=20, blank=True, default="0 USD")
    dash_status = models.CharField(max_length=20, blank=True, default="success")
    dash_gateway = models.CharField(max_length=20, blank=True, default="system")
    

    dash_description1 = models.CharField(max_length=20, blank=True, default="")
    dash_transactionID1 = models.CharField(max_length=20, blank=True, default="")
    dash_type1 = models.CharField(max_length=20, blank=True, default="")
    dash_amount1 = models.CharField(max_length=20, blank=True, default="")
    dash_fee1 = models.CharField(max_length=20, blank=True, default="")
    dash_status1 = models.CharField(max_length=20, blank=True, default="")
    dash_gateway1 = models.CharField(max_length=20, blank=True, default="")
    

    dash_description2 = models.CharField(max_length=20, blank=True, default="")
    dash_transactionID2 = models.CharField(max_length=20, blank=True, default="")
    dash_type2 = models.CharField(max_length=20, blank=True, default="")
    dash_amount2 = models.CharField(max_length=20, blank=True, default="")
    dash_fee2 = models.CharField(max_length=20, blank=True, default="")
    dash_status2 = models.CharField(max_length=20, blank=True, default="")
    dash_gateway2 = models.CharField(max_length=20, blank=True, default="")
    

    dash_description3 = models.CharField(max_length=20, blank=True, default="")
    dash_transactionID3 = models.CharField(max_length=20, blank=True, default="")
    dash_type3 = models.CharField(max_length=20, blank=True, default="")
    dash_amount3 = models.CharField(max_length=20, blank=True, default="")
    dash_fee3 = models.CharField(max_length=20, blank=True, default="")
    dash_status3 = models.CharField(max_length=20, blank=True, default="")
    dash_gateway3 = models.CharField(max_length=20, blank=True, default="")





    schema_icon_default = models.CharField(max_length=20, blank=True, default="")
    schema_schema_default = models.CharField(max_length=20, blank=True, default="")
    schema_ROI = models.CharField(max_length=20, blank=True, default="")
    schema_profit = models.CharField(max_length=20, blank=True, default="")
    schema_period_remaining = models.CharField(max_length=20, blank=True, default="")
    schema_capital_back = models.CharField(max_length=20, blank=True, default="")
    schema_timeline = models.CharField(max_length=20, blank=True, default="")
    

    schema_icon1 = models.CharField(max_length=20, blank=True, default="")
    schema_schema1 = models.CharField(max_length=20, blank=True, default="")
    schema_ROI1 = models.CharField(max_length=20, blank=True, default="")
    schema_profit1 = models.CharField(max_length=20, blank=True, default="")
    schema_period_remaining1 = models.CharField(max_length=20, blank=True, default="")
    schema_capital_back1 = models.CharField(max_length=20, blank=True, default="")
    schema_timeline1 = models.CharField(max_length=20, blank=True, default="")
    

    schema_icon2 = models.CharField(max_length=20, blank=True, default="")
    schema_schema2 = models.CharField(max_length=20, blank=True, default="")
    schema_ROI2 = models.CharField(max_length=20, blank=True, default="")
    schema_profit2 = models.CharField(max_length=20, blank=True, default="")
    schema_period_remaining2 = models.CharField(max_length=20, blank=True, default="")
    schema_capital_back2 = models.CharField(max_length=20, blank=True, default="")
    schema_timeline2 = models.CharField(max_length=20, blank=True, default="")
    
    schema_icon3 = models.CharField(max_length=20, blank=True, default="")
    schema_schema3 = models.CharField(max_length=20, blank=True, default="")
    schema_ROI3 = models.CharField(max_length=20, blank=True, default="")
    schema_profit3 = models.CharField(max_length=20, blank=True, default="")
    schema_period_remaining3 = models.CharField(max_length=20, blank=True, default="")
    schema_capital_back3 = models.CharField(max_length=20, blank=True, default="")
    schema_timeline3 = models.CharField(max_length=20, blank=True, default="")

    
    schema_icon4 = models.CharField(max_length=20, blank=True, default="")
    schema_schema4 = models.CharField(max_length=20, blank=True, default="")
    schema_ROI4 = models.CharField(max_length=20, blank=True, default="")
    schema_profit4 = models.CharField(max_length=20, blank=True, default="")
    schema_period_remaining4 = models.CharField(max_length=20, blank=True, default="")
    schema_capital_back4 = models.CharField(max_length=20, blank=True, default="")
    schema_timeline4 = models.CharField(max_length=20, blank=True, default="")








    transaction_description_default = models.CharField(max_length=20, blank=True, default="signup bonus")
    transaction_transactionID_default = models.CharField(max_length=20, blank=True, default="TRXYLNKPNUR5K")
    transaction_type = models.CharField(max_length=20, blank=True, default="signup bonus")
    transaction_amount = models.CharField(max_length=20, blank=True, default="+5 USD")
    transaction_fee = models.CharField(max_length=20, blank=True, default="0 USD")
    transaction_status = models.CharField(max_length=20, blank=True, default="success")
    transaction_gateway = models.CharField(max_length=20, blank=True, default="system")
    

    transaction_description1 = models.CharField(max_length=20, blank=True, default="")
    transaction_transactionID1 = models.CharField(max_length=20, blank=True, default="")
    transaction_type1 = models.CharField(max_length=20, blank=True, default="")
    transaction_amount1 = models.CharField(max_length=20, blank=True, default="")
    transaction_fee1 = models.CharField(max_length=20, blank=True, default="")
    transaction_status1 = models.CharField(max_length=20, blank=True, default="")
    transaction_gateway1 = models.CharField(max_length=20, blank=True, default="")
    

    transaction_description2 = models.CharField(max_length=20, blank=True, default="")
    transaction_transactionID2 = models.CharField(max_length=20, blank=True, default="")
    transaction_type2 = models.CharField(max_length=20, blank=True, default="")
    transaction_amount2 = models.CharField(max_length=20, blank=True, default="")
    transaction_fee2 = models.CharField(max_length=20, blank=True, default="")
    transaction_status2 = models.CharField(max_length=20, blank=True, default="")
    transaction_gateway2 = models.CharField(max_length=20, blank=True, default="")
    

    transaction_description3 = models.CharField(max_length=20, blank=True, default="")
    transaction_transactionID3 = models.CharField(max_length=20, blank=True, default="")
    transaction_type3 = models.CharField(max_length=20, blank=True, default="")
    transaction_amount3 = models.CharField(max_length=20, blank=True, default="")
    transaction_fee3 = models.CharField(max_length=20, blank=True, default="")
    transaction_status3 = models.CharField(max_length=20, blank=True, default="")
    transaction_gateway3 = models.CharField(max_length=20, blank=True, default="")

    
    transaction_description4 = models.CharField(max_length=20, blank=True, default="")
    transaction_transactionID4 = models.CharField(max_length=20, blank=True, default="")
    transaction_type4 = models.CharField(max_length=20, blank=True, default="")
    transaction_amount4 = models.CharField(max_length=20, blank=True, default="")
    transaction_fee4 = models.CharField(max_length=20, blank=True, default="")
    transaction_status4 = models.CharField(max_length=20, blank=True, default="")
    transaction_gateway4 = models.CharField(max_length=20, blank=True, default="")






    add_money_description_default = models.CharField(max_length=20, blank=True, default="")
    add_money_transactionID_default = models.CharField(max_length=20, blank=True, default="")
    add_money_amount = models.CharField(max_length=20, blank=True, default="")
    add_money_fee = models.CharField(max_length=20, blank=True, default="")
    add_money_status = models.CharField(max_length=20, blank=True, default="")
    add_money_gateway = models.CharField(max_length=20, blank=True, default="")
    

    add_money_description1 = models.CharField(max_length=20, blank=True, default="")
    add_money_transactionID1 = models.CharField(max_length=20, blank=True, default="")
    add_money_amount1 = models.CharField(max_length=20, blank=True, default="")
    add_money_fee1 = models.CharField(max_length=20, blank=True, default="")
    add_money_status1 = models.CharField(max_length=20, blank=True, default="")
    add_money_gateway1 = models.CharField(max_length=20, blank=True, default="")
    

    add_money_description2 = models.CharField(max_length=20, blank=True, default="")
    add_money_transactionID2 = models.CharField(max_length=20, blank=True, default="")
    add_money_amount2 = models.CharField(max_length=20, blank=True, default="")
    add_money_fee2 = models.CharField(max_length=20, blank=True, default="")
    add_money_status2 = models.CharField(max_length=20, blank=True, default="")
    add_money_gateway2 = models.CharField(max_length=20, blank=True, default="")
    
    add_money_description3 = models.CharField(max_length=20, blank=True, default="")
    add_money_transactionID3 = models.CharField(max_length=20, blank=True, default="")
    add_money_amount3 = models.CharField(max_length=20, blank=True, default="")
    add_money_fee3 = models.CharField(max_length=20, blank=True, default="")
    add_money_status3 = models.CharField(max_length=20, blank=True, default="")
    add_money_gateway3 = models.CharField(max_length=20, blank=True, default="")

    
    add_money_description4 = models.CharField(max_length=20, blank=True, default="")
    add_money_transactionID4 = models.CharField(max_length=20, blank=True, default="")
    add_money_amount4 = models.CharField(max_length=20, blank=True, default="")
    add_money_fee4 = models.CharField(max_length=20, blank=True, default="")
    add_money_status4 = models.CharField(max_length=20, blank=True, default="")
    add_money_gateway4 = models.CharField(max_length=20, blank=True, default="")
    


    withdraw_description_default = models.CharField(max_length=20, blank=True, default="")
    withdraw_transactionID_default = models.CharField(max_length=20, blank=True, default="")
    withdraw_amount = models.CharField(max_length=20, blank=True, default="")
    withdraw_fee = models.CharField(max_length=20, blank=True, default="")
    withdraw_status = models.CharField(max_length=20, blank=True, default="")
    withdraw_gateway = models.CharField(max_length=20, blank=True, default="")
    

    withdraw_description1 = models.CharField(max_length=20, blank=True, default="")
    withdraw_transactionID1 = models.CharField(max_length=20, blank=True, default="")
    withdraw_amount1 = models.CharField(max_length=20, blank=True, default="")
    withdraw_fee1 = models.CharField(max_length=20, blank=True, default="")
    withdraw_status1 = models.CharField(max_length=20, blank=True, default="")
    withdraw_gateway1 = models.CharField(max_length=20, blank=True, default="")
    

    withdraw_description2 = models.CharField(max_length=20, blank=True, default="")
    withdraw_transactionID2 = models.CharField(max_length=20, blank=True, default="")
    withdraw_amount2 = models.CharField(max_length=20, blank=True, default="")
    withdraw_fee2 = models.CharField(max_length=20, blank=True, default="")
    withdraw_status2 = models.CharField(max_length=20, blank=True, default="")
    withdraw_gateway2 = models.CharField(max_length=20, blank=True, default="")
    
    withdraw_description3 = models.CharField(max_length=20, blank=True, default="")
    withdraw_transactionID3 = models.CharField(max_length=20, blank=True, default="")
    withdraw_amount3 = models.CharField(max_length=20, blank=True, default="")
    withdraw_fee3 = models.CharField(max_length=20, blank=True, default="")
    withdraw_status3 = models.CharField(max_length=20, blank=True, default="")
    withdraw_gateway3 = models.CharField(max_length=20, blank=True, default="")

    
    withdraw_description4 = models.CharField(max_length=20, blank=True, default="")
    withdraw_transactionID4 = models.CharField(max_length=20, blank=True, default="")
    withdraw_amount4 = models.CharField(max_length=20, blank=True, default="")
    withdraw_fee4 = models.CharField(max_length=20, blank=True, default="")
    withdraw_status4 = models.CharField(max_length=20, blank=True, default="")
    withdraw_gateway4 = models.CharField(max_length=20, blank=True, default="")




    
    


    def __str__(self):
        return f"Account Balance for {self.user.username}"
