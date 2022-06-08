# Generated by Django 4.0.4 on 2022-05-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0003_alter_data_encryption_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email of user'),
        ),
    ]
