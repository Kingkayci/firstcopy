from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import UploadedReceipt, UploadKYC, ContactForm

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['contact_name', 'contact_email', 'contact_subject', 'contact_message']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contact_name"].widget.attrs.update({
            "type":"text", 
            "placeholder": "Name", 
            "maxlength":"40", 
            "minlength":"5",
        })

        self.fields["contact_email"].widget.attrs.update({
            "type":"email", 
            "placeholder":"Email",  
            "maxlength":"40", 
            "minlength":"5",
        })
        
        self.fields["contact_subject"].widget.attrs.update({
            "type":"text",
            "placeholder": "Subject",  
            "maxlength":"40", 
            "minlength":"5",
        })

        self.fields["contact_message"].widget.attrs.update({
            "type":"text",
            "placeholder": "Your Message",  
            "maxlength":"999", 
            "minlength":"5",
            "row": "4"
        })





class ReceiptUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedReceipt
        fields = ['username', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text", 
            "class":"receipt-input",  
            "maxlength":"16", 
            "minlength":"5",
        })


class KYCUploadForm(forms.ModelForm):
    class Meta:
        model = UploadKYC
        fields = ['card', 'imagePassport']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["card"].widget.attrs.update({
            "class":"card-input",  
        })

        self.fields["imagePassport"].widget.attrs.update({
            "class":"passport-input",  
        })



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    
    referral = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "phone", "referral")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")

        return password2
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "type":"text", 
            "id":"firstname", 
            "class":"box-input", 
            "placeholder":"Enter First Name", 
            "maxlength":"16", 
            "minlength":"5",
        })


        self.fields["last_name"].widget.attrs.update({
            "type":"text", 
            "id":"lastname", 
            "class":"box-input", 
            "placeholder":"Referral Code", 
            "maxlength":"100", 
            "minlength":"5",
        })

        self.fields["username"].widget.attrs.update({
            "type":"text", 
            "id":"username", 
            "class":"box-input", 
            "placeholder":"Enter Unique Username", 
            "maxlength":"16", 
            "minlength":"3",
        })

    
        self.fields["email"].widget.attrs.update({
            "type":"email", 
            "id":"email", 
            "class":"box-input", 
            "placeholder":"name@example.com", 
            "maxlength":"30", 
            "minlength":"6",
        })
        
        self.fields["phone"].widget.attrs.update({
            "type":"number", 
            "id":"phone", 
            "class":"box-input", 
            "placeholder":"Enter Phone No.", 
            "maxlength":"30", 
            "minlength":"6",
        })

        
        self.fields["referral"].widget.attrs.update({
            "type":"text", 
            "id":"referral", 
            "class":"box-input", 
            "placeholder":"Enter Optional Referral Code", 
            "maxlength":"16", 
            "minlength":"5",
        })



        self.fields["password1"].widget.attrs.update({
            "type":"password", 
            "id":"password1", 
            "class":"box-input", 
            "placeholder":"Enter Password", 
            "maxlength":"30", 
            "minlength":"6",
        })


        self.fields["password2"].widget.attrs.update({
            "type":"password", 
            "id":"password2", 
            "class":"box-input", 
            "placeholder":"Confirm Password", 
            "maxlength":"30", 
            "minlength":"6",
        })


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user