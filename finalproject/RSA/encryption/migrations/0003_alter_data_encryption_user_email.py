# Generated by Django 4.0.4 on 2022-05-11 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0002_alter_users_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_encryption',
            name='user_email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='encryption.users'),
            preserve_default=False,
        ),
    ]
