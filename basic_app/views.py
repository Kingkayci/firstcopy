from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AccountBalance
from django.contrib.auth.decorators import login_required
from .forms import ReceiptUploadForm, KYCUploadForm, ContactUsForm

# Create your views here.

def contact_form(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:contact-success')
    else:
        form = ContactUsForm()
    return render(request, template_name='contact-us.html', context={'contact':form})



def upload_receipt(request):
    if request.method == 'POST':
        form = ReceiptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:user-verify-receipt')
    else:
        form = ReceiptUploadForm()

    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/deposit.html', context={'account_balance':account_balance, 'receipt_form':form})


def upload_kyc(request):
    if request.method == "POST":
        form = KYCUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:user-verify-kyc')
    else:
        form = KYCUploadForm()

    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/kyc.html', context={'account_balance':account_balance, 'kyc_form':form})






@login_required
def user_dashboard_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/dashboard.html', context={'account_balance':account_balance})


@login_required
def user_schemaLogs_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/schema-logs.html', context={'account_balance':account_balance})


@login_required
def user_withdrawLogs_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/withdraw-logs.html', context={'account_balance':account_balance})


@login_required
def user_depositLogs_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/deposit-logs.html', context={'account_balance':account_balance})



@login_required
def user_deposit_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/deposit.html', context={'account_balance':account_balance})


@login_required
def user_rankingBadge_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/ranking-badge.html', context={'account_balance':account_balance})

@login_required
def user_referral_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/referral.html', context={'account_balance':account_balance})

@login_required
def user_schemas_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/schemas.html', context={'account_balance':account_balance})

@login_required
def user_transactions_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/transactions.html', context={'account_balance':account_balance})

@login_required
def user_verifyKyc_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/verify-kyc.html', context={'account_balance':account_balance})

@login_required
def user_verifyReceipt_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/verify-receipt.html', context={'account_balance':account_balance})

@login_required
def user_withdraw_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/withdraw.html', context={'account_balance':account_balance})






@login_required
def user_active_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/active.html', context={'account_balance':account_balance})

@login_required
def user_commission_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/commission-fee.html', context={'account_balance':account_balance})


@login_required
def user_conversion_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/conversion-fee.html', context={'account_balance':account_balance})

@login_required
def user_topup_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/top-up.html', context={'account_balance':account_balance})

@login_required
def user_pending_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user

    # Pass the account_balance instance to the template
    return render(request, template_name='user/pending.html', context={'account_balance':account_balance})





def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('basic_app:user-dashboard')
        else:
            messages.error(request, 'Invalid username and/or password')

    form = AuthenticationForm()
    return render(request, template_name='login.html', context={'login':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('basic_app:login')

class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('basic_app:user-dashboard-first')
    template_name = 'form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class HomePage(TemplateView):
    template_name = 'index.html'

class SchemaPage(TemplateView):
    template_name = 'schema.html'

class RankingsPage(TemplateView):
    template_name = 'rankings.html'

class HowItWorks(TemplateView):
    template_name = 'how-it-works.html'

class AboutUs(TemplateView):
    template_name = 'about-us.html'

class Blog(TemplateView):
    template_name = 'blog.html'

class PrivacyPolicy(TemplateView):
    template_name = 'privacy.html'

class FAQ(TemplateView):
    template_name = 'faq.html'

class TermsAndConditions(TemplateView):
    template_name = 'terms-conditions.html'

class BlogFirst(TemplateView):
    template_name = 'blog-first.html'

class BlogSecond(TemplateView):
    template_name = 'blog-second.html'

class ContactSuccess(TemplateView):
    template_name = 'contact-us-success.html'

class UserDashboardFirst(TemplateView):
    template_name = 'user/dashboard-first.html'



