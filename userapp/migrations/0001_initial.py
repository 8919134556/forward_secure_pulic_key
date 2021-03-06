# Generated by Django 3.2.8 on 2022-06-01 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_file',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(db_column='user_name', max_length=50, verbose_name='User_Name')),
                ('gender', models.CharField(db_column='gender', max_length=50, verbose_name='Gender')),
                ('city', models.CharField(db_column='city', max_length=50, null=True, verbose_name='City')),
                ('addres', models.CharField(db_column='addres', max_length=50, verbose_name='Addres')),
                ('user_email', models.EmailField(blank=True, db_column='user_email', max_length=100, null=True, verbose_name='User_Email')),
                ('user_pwd', models.CharField(db_column='user_pwd', max_length=100, verbose_name='User_Password')),
                ('user_file', models.FileField(blank=True, db_column='user_file', upload_to='User/Files/', verbose_name='User_File')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Upload_file',
            },
        ),
    ]
