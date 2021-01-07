from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
	IN_PROGRESS = 0
	SUCCESS = 1
	FAIL = 2
	STATUS_CHOICES = (
		(IN_PROGRESS, 'In Progress'),
		(SUCCESS, 'Success'),
		(FAIL, 'Skipped'),
	)

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200, blank=False)
	date_created = models.DateTimeField('date_made', null=False, blank=False, default=datetime.now)
	status = models.IntegerField(default=IN_PROGRESS, choices=STATUS_CHOICES)

	def __str__(self):
		return self.title