# Generated by Django 3.2.8 on 2022-06-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_request_token_post_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_token',
            name='post_token',
            field=models.CharField(blank=True, db_column='post_token', default='Pending', max_length=50, null='True', verbose_name='Post_Token'),
        ),
    ]
