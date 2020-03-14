# Generated by Django 3.0.4 on 2020-03-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200312_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomeraccount',
            name='govt_id',
            field=models.CharField(choices=[('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('other', 'OTHER')], max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='useremployeeaccount',
            name='govt_id',
            field=models.CharField(choices=[('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('other', 'OTHER')], max_length=150, null=True, unique=True),
        ),
    ]
