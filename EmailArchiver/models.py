# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django_mailbox.signals import message_received
from django.dispatch import receiver

class MailStorage(models.Model):
	sender = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	date = models.DateTimeField('date_recieved')
	body = models.TextField('Body')
	
	def __str__(self):
		return self.subject


class Login(models.Model):
	username = models.EmailField(max_length=254)
	password = models.CharField(max_length=255)

        def __str__(self):
                return self.username


