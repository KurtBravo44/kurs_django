# Generated by Django 5.0 on 2023-12-11 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=100, verbose_name='тема письма')),
                ('message_body', models.TextField(verbose_name='тело письма')),
                ('start', models.DateTimeField(verbose_name='начало')),
                ('stop', models.DateTimeField(verbose_name='конец')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Еженедельная'), ('monthly', 'Ежемесячная')], default='daily', max_length=25, verbose_name='период')),
                ('status', models.CharField(blank=True, max_length=25, null=True, verbose_name='статус')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='LogMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_try', models.DateTimeField(blank=True, null=True, verbose_name='последняя попытка')),
                ('status_try', models.CharField(blank=True, max_length=25, null=True, verbose_name='статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
                ('mailing_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
