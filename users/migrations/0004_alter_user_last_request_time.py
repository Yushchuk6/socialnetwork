# Generated by Django 3.2.4 on 2021-06-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_last_request_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_request_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
