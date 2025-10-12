from django.urls import path
from basic_app import views


app_name = "basic_app"

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("user/kyc/", views.upload_kyc, name="kyc"),
    path("user/deposit/", views.upload_receipt, name="user-deposit"),
    path('user/dashboard/', views.user_dashboard_view, name='user-dashboard'),
    path('user/schema/logs/', views.user_schemaLogs_view, name='user-schema-logs'),
    path('user/deposit/logs/', views.user_depositLogs_view, name='user-deposit-logs'),
    path('user/ranking/', views.user_rankingBadge_view, name='user-ranking'),
    path('user/referral/', views.user_referral_view, name='user-referral'),
    path('user/schemas/', views.user_schemas_view, name='user-schemas'),
    path('user/transactions/', views.user_transactions_view, name='user-transactions'),
    path('user/kyc-verification/', views.user_verifyKyc_view, name='user-verify-kyc'),
    path('user/receipt-confirmation/', views.user_verifyReceipt_view, name='user-verify-receipt'),
    path('user/withdraw/logs/', views.user_withdrawLogs_view, name='user-withdraw-logs'),
    path('user/withdraw/', views.user_withdraw_view, name='user-withdraw'),
    path('user/dashboard-first/', views.UserDashboardFirst.as_view(), name='user-dashboard-first'),
    path('user/dashboard/active/', views.user_active_view, name='user-active'),
    path('user/dashboard/commission-fee/', views.user_commission_view, name='user-commission-fee'),
    path('user/dashboard/conversion-fee/', views.user_conversion_view, name='user-conversion-fee'),
    path('user/dashboard/top-up-fee/', views.user_topup_view, name='user-topup'),
    path('user/dashboard/pending/', views.user_pending_view, name='user-pending'),

    path("schema/", views.SchemaPage.as_view(), name='schema'),
    path("rankings/", views.RankingsPage.as_view(), name='rankings'),
    path("how-it-works/", views.HowItWorks.as_view(), name="how-it-works"),
    path("about-us/", views.AboutUs.as_view(), name='about-us'),
    path("blog/", views.Blog.as_view(), name='blog'),
    path("contact-us/", views.contact_form, name='contact'),
    path("contact-us/success", views.ContactSuccess.as_view(), name='contact-success'),
    path("privacy-policy/", views.PrivacyPolicy.as_view(), name='privacy'),
    path("faq/", views.FAQ.as_view(), name='faq'),
    path("terms-conditions/", views.TermsAndConditions.as_view(), name='terms'),
    path("blog/1/", views.BlogFirst.as_view(), name='blog-first'),
    path("blog/2/", views.BlogSecond.as_view(), name='blog-second'),
    path("register/", views.SignUpView.as_view(), name='register'),
    path("login/", views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout'),

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)