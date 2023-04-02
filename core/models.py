from django.db import models

# Create your models here.

class NewsItem(models.Model):
	source = models.CharField(max_length=100)
	link = models.TextField()
	title = models.CharField(max_length=200)
	published_date = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class ScrapeHistory(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	finished_time = models.DateTimeField()
	finished = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.timestamp}"