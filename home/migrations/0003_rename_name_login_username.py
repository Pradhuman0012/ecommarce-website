# Generated by Django 4.1.2 on 2022-10-29 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_pwd_login_password_rename_mobile_login_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='username',
        ),
    ]
