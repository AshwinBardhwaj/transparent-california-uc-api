# Generated by Django 5.0.1 on 2024-01-08 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TransparentCaliforniaUC', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ucemployee',
            old_name='benefits',
            new_name='Benefits',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='benefits_currency',
            new_name='Benefits_currency',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='job_title',
            new_name='Job_Title',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='other_pay',
            new_name='Other_Pay',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='other_pay_currency',
            new_name='Other_Pay_currency',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='overtime_pay',
            new_name='Overtime_Pay',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='overtime_pay_currency',
            new_name='Overtime_Pay_currency',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='regular_pay',
            new_name='Regular_Pay',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='regular_pay_currency',
            new_name='Regular_Pay_currency',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='total_pay',
            new_name='Total_Pay',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='total_pay_and_benefits',
            new_name='Total_Pay_And_Benefits',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='total_pay_and_benefits_currency',
            new_name='Total_Pay_And_Benefits_currency',
        ),
        migrations.RenameField(
            model_name='ucemployee',
            old_name='total_pay_currency',
            new_name='Total_Pay_currency',
        ),
    ]
