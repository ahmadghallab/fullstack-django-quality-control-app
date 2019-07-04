from django.contrib import admin

from . import models

admin.site.register(models.Place)
admin.site.register(models.Major)
admin.site.register(models.Employee)
admin.site.register(models.Criteria)
admin.site.register(models.BasicEvaluation)
admin.site.register(models.MemberEvaluation)
admin.site.register(models.TicketEvaluation)
admin.site.register(models.SurveyEvaluation)