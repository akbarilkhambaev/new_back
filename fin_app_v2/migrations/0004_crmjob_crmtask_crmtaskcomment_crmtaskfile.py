# Generated by Django 5.1.1 on 2025-06-08 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_app_v2', '0003_task_confirmation_date_task_confirmed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrmJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('client_email', models.EmailField(max_length=254)),
                ('over_all_income', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(blank=True, default='', max_length=255, verbose_name='ФИО')),
                ('phone_number', models.CharField(blank=True, default='', max_length=32, verbose_name='Номер телефона')),
                ('position', models.CharField(blank=True, choices=[('Менеджер', 'Менеджер'), ('Директор', 'Директор')], default='', max_length=32, verbose_name='Позиция')),
                ('client_company_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Название клиентской компании')),
                ('client_company_phone', models.CharField(blank=True, default='', max_length=32, verbose_name='Номер телефона клиентской компании')),
                ('client_company_address', models.CharField(blank=True, default='', max_length=255, verbose_name='Адрес клиентской компании')),
                ('client_website', models.CharField(blank=True, default='', max_length=255, verbose_name='Адрес веб-сайта')),
            ],
        ),
        migrations.CreateModel(
            name='CrmTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crm_tasks', to='fin_app_v2.crmjob')),
            ],
        ),
        migrations.CreateModel(
            name='CrmTaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crm_comments', to='fin_app_v2.crmtask')),
            ],
        ),
        migrations.CreateModel(
            name='CrmTaskFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='task_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crm_files', to='fin_app_v2.crmtask')),
            ],
        ),
    ]
