from django.contrib import admin

# Register your models here.

from teamapp.models import Tag, Vacancy,Otklik, TagAssign
from users.models import User, CustomerProfile
class TagInline(admin.TabularInline):
	model = Tag


class TagAssignInline(admin.TabularInline):
	model = TagAssign

class VacancyAdmin(admin.ModelAdmin):
	inlines = [
		TagAssignInline,
	]

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Tag)
admin.site.register(TagAssign)


class ProfileInline(admin.StackedInline):
	model = CustomerProfile

class UserAdmin(admin.ModelAdmin):
	inlines = [
		ProfileInline,
	]

admin.site.register(User, UserAdmin)
admin.site.register(Otklik)
