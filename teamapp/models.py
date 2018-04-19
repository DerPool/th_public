from django.db import models
from teams.models import Tag
from users.models import User, CustomerProfile


class Vacancy(models.Model):
	STATUSES = (
		("O", "Открыта"),
		("M", "Модерация"),
		("C", "Закрыта")
	)
	creator = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
	short_desc = models.CharField(max_length=100)
	desc = models.CharField(max_length=500)
	dateofcreation = models.DateTimeField()
	status = models.CharField(max_length=1, choices=STATUSES)

	def __str__(self):
		return str(self.pk) + " " + self.creator.surname + ": " + self.short_desc
# Create your models here.


class TagAssign(models.Model):
	VALUE_CHOICES = (
		("3", "Критично"),
		("2","Важно"),
		("1","Желательно")
	)
	vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	value  = models.CharField(max_length=10, choices = VALUE_CHOICES)


class Otklik(models.Model):
	STATUSES = (
		("P", "Ожидание"),
		("A", "Согласие"),
		("D", "Отклонено")
	)
	user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
	target = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	target_user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField()
	status = models.CharField(max_length=1, choices=STATUSES)

	def __str__(self):
		return self.user.surname + "-" + self.target.short_desc