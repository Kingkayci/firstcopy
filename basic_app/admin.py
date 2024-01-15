from django.contrib import admin
from .models import UploadedReceipt, UploadKYC, AccountBalance, ContactForm

# Register your models here.
admin.site.register(UploadedReceipt)
admin.site.register(UploadKYC)
admin.site.register(AccountBalance)
admin.site.register(ContactForm)