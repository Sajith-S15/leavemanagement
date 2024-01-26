from django.db import models
from django.db.models.deletion import CASCADE

from django.forms import DateTimeField
from apps.users.models import User
from config.constants import LEAVE_TYPE, LEAVE_STATUS, APPLIED_TO


class Leave(models.Model):
    class Meta(object):
        db_table = 'leave'

    user_name = models.ForeignKey(
        User, on_delete=CASCADE, blank=False, null=False, related_name='Username'
    )
    
    

    leave_type = models.CharField(
        'Leave Type', blank=False, null=False, default='N/A', choices=LEAVE_TYPE, max_length=40
    )

    leave_balance = models.IntegerField(
        'Leave Balance', blank=False, null=False, default=0
    )

    from_date = models.DateTimeField(
        'From Date', blank=False, null=False

    )
    to_date = models.DateTimeField(
        'To Date', blank=False, null=False
    )

    duration = models.IntegerField(
        'Duration', blank=False, null=False, default=0
    )

    applied_to = models.CharField(
        'Applied To', blank=False, null=False, default='Rajeswari', choices=APPLIED_TO, max_length=550

    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=False, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated Datetime', blank=False, auto_now=True
    )
    description = models.CharField(
        'Notes', blank=False, null=False, db_index=True, max_length=400, default='Description & Responsibilities Assigned'
    )
    leave_status = models.CharField(
        'Leave Status', blank=True, null=True, default='N/A', choices=LEAVE_STATUS, max_length=40

    )

    def __str__(self):
        return str(self.user_name)
