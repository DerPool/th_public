from django.db import models

class Tag(models.Model):
	tag = models.CharField(max_length=15)

	def __str__(self):
		return self.tag




# Create your models here.