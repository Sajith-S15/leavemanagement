# Generated by Django 4.1.4 on 2024-01-26 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('n/a', 'N/A'), ('casual_leave', 'Casual Leave'), ('sick_leave', 'Sick Leave'), ('maternity_leave', 'Maternity Leave'), ('paternity_leave', 'Paternity Leave'), ('loss_of_pay_leave', 'Loss of Pay'), ('emergency', 'Emergency Leave')], default='N/A', max_length=40, verbose_name='Leave Type')),
                ('leave_balance', models.IntegerField(default=0, verbose_name='Leave Balance')),
                ('from_date', models.DateTimeField(verbose_name='From Date')),
                ('to_date', models.DateTimeField(verbose_name='To Date')),
                ('duration', models.IntegerField(default=0, verbose_name='Duration')),
                ('applied_to', models.CharField(choices=[('rajeshwari', 'Rajeshwari'), ('saravana_kumar', 'Saravana Kumar'), ('hr', 'HR TECH IS')], default='Rajeswari', max_length=550, verbose_name='Applied To')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('description', models.CharField(db_index=True, default='Description & Responsibilities Assigned', max_length=400, verbose_name='Notes')),
                ('leave_status', models.CharField(blank=True, choices=[('applied', 'Applied'), ('req_modification', 'Request Modification'), ('forwarded', 'Forwarded'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='N/A', max_length=40, null=True, verbose_name='Leave Status')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Username', to='users.user')),
            ],
            options={
                'db_table': 'leave',
            },
        ),
    ]
