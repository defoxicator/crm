# Generated by Django 4.0.5 on 2022-07-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='def_pic.jpg', null=True, upload_to=''),
        ),
    ]