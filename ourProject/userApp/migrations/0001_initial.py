# Generated by Django 5.0 on 2024-01-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(max_length=100)),
                ('user_username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_phone_number', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]