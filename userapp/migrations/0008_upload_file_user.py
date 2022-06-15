# Generated by Django 3.2.8 on 2022-06-02 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_user_register_user_image'),
        ('userapp', '0007_alter_upload_file_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_file',
            name='user',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.user_register'),
        ),
    ]