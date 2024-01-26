# Generated by Django 4.1.4 on 2024-01-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Employee ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50, verbose_name='Status')),
                ('name', models.CharField(max_length=50, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('shifts', models.CharField(choices=[('n/a', 'N/A'), ('day', 'Day'), ('night', 'Night'), ('afternoon', 'Afternoon')], default='N/A', max_length=50, verbose_name='Shifts')),
                ('token', models.CharField(max_length=500, verbose_name='Token')),
                ('token_expires_at', models.DateTimeField(max_length=50, verbose_name='Token Expires at')),
                ('role', models.CharField(choices=[('director', 'Director'), ('manager', 'Manager'), ('leader', 'Leader'), ('member', 'Member'), ('co-ordinator', 'Co-Ordinator')], max_length=50, verbose_name='Role')),
                ('team', models.CharField(choices=[('director', 'Director'), ('marketer', 'Marketer'), ('engineer', 'Engineer'), ('hr', 'HR'), ('sales', 'Sales'), ('admin', 'Admin'), ('communication', 'Communication')], max_length=50, verbose_name='Team')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
