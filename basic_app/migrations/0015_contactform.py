# Generated by Django 5.0 on 2024-01-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0014_rename_dash_deposit_bonus_accountbalance_dash_signup_bonus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=100)),
                ('contact_subject', models.CharField(max_length=100)),
                ('contact_message', models.CharField(max_length=900)),
            ],
        ),
    ]