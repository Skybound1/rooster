from django.contrib import admin

from .models import ConstraintDescription, JobDescription, Event, Volunteer, \
    Job


@admin.register(ConstraintDescription)
class ConstraintDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
