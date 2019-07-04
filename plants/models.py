from django.db import models
from django.utils import timezone


class Place(models.Model):
    ar_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ar_name

class EvaluationType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class Major(models.Model):
    ar_name = models.CharField(max_length=255, unique=True)
    evaluation_type = models.ForeignKey(EvaluationType, related_name='major_evaluation_type', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ar_name

class Employee(models.Model):
    place = models.ForeignKey(Place, related_name='employee_place', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, related_name='employee_major', on_delete=models.CASCADE, null=True, blank=True)
    evaluation_type = models.ForeignKey(EvaluationType, related_name='employee_evaluation_type', on_delete=models.CASCADE, null=True, blank=True)
    ar_name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    join_year = models.IntegerField(null=True, blank=True)
    positive_score = models.IntegerField(default=0)
    negative_score = models.IntegerField(default=0)

    class Meta:
        unique_together = ("place", "ar_name")

    def __str__(self):
        return self.ar_name

class Criteria(models.Model):
    major = models.ForeignKey(Major, related_name='criteria_department', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    solution = models.CharField(max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{0.description} for major {0.major}'.format(self)

class Evaluation(models.Model):
    place = models.ForeignKey(Place, related_name='result_place', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, related_name='result_major', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='result_employee', on_delete=models.CASCADE, null=True)
    criteria = models.ForeignKey(Criteria, related_name='result_criteria', on_delete=models.CASCADE)
    notes = models.TextField(max_length=255, blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return '{0.criteria}'.format(self)

class BasicEvaluation(Evaluation):
    yes_or_no = models.IntegerField(default=0)

class MemberEvaluation(models.Model):
    place = models.ForeignKey(Place, related_name='employee_evaluation_place', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, related_name='employee_evaluation_major', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, related_name='employee_evaluation_employee_name', on_delete=models.CASCADE, null=True)
    criteria = models.ForeignKey(Criteria, related_name='employee_evaluation_criteria', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    evaluation_score = models.IntegerField()

    def __str__(self):
        return '{0.criteria} | {0.employee}'.format(self)

class TicketEvaluation(models.Model):
    ticket_number = models.IntegerField(default=0)
    place = models.ForeignKey(Place, related_name='ticket_evaluation_place', on_delete=models.CASCADE, null=True)
    major = models.ForeignKey(Major, related_name='ticket_evaluation_major', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, related_name='ticket_evaluation_employee', on_delete=models.CASCADE, null=True)
    criteria = models.ForeignKey(Criteria, related_name='ticket_evaluation_criteria', on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    yes_or_no = models.IntegerField(default=0)

    def __str__(self):
        return '{0.criteria} ticket No. {0.ticket_number}'.format(self)

class SurveyEvaluation(models.Model):
    voter_name = models.TextField()
    voter_age = models.TextField()
    place = models.ForeignKey(Place, related_name='survey_evaluation_place', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, related_name='survey_evaluation_major', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='survey_evaluation_employee', on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, related_name='survey_evaluation_criteria', on_delete=models.CASCADE)
    evaluation_score = models.IntegerField()
    notes = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return '{0.voter_name} {0.evaluation_score} {0.employee}'.format(self)