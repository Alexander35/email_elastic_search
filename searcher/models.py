from django.db import models
from .search import EmailIndex

# Create your models here.

class Email(models.Model):
	title = models.CharField(max_length=200, default=None, blank=True, null=True)
	sender = models.CharField(max_length=200, default=None, blank=True, null=True)
	date = models.CharField(max_length=200, default=None, blank=True, null=True)
	text = models.TextField(max_length=1000, default=None, blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	def indexing(self):
		obj = EmailIndex(
			meta = {'id': self.id},
			title = self.title,
			sender = self.sender,
			date = self.date,
			text = self.text
		)
		obj.save()

		return obj.to_dict(include_meta=True)

	def __str__(self):
		return '{} | {}'.format(self.title, self.date)		