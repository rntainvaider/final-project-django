# Generated by Django 4.2.18 on 2025-02-14 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Роль пользователя',
                'verbose_name_plural': 'Роли пользователей',
                'db_table': 'users_role',
            },
        ),
        migrations.CreateModel(
            name='CustomUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=55, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=55, verbose_name='Имя')),
                ('midle_name', models.CharField(max_length=55, verbose_name='Отчество')),
                ('phone_name', models.CharField(max_length=18, verbose_name='Телефон')),
                ('email', models.CharField(max_length=128, verbose_name='Email')),
                ('password', models.CharField(max_length=128)),
                ('role', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userrole', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
            },
        ),
    ]
