from django.core import serializers
from django.views import generic
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.db.models import Count, Sum, F, Q, FloatField
from django.db.models.functions import Cast
from django.urls import reverse
from datetime import datetime
import pygal
from pygal.style import Style

from . import forms
from . import models

# Place Views
class PlaceCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.PlaceForm
    model = models.Place

    success_url = '/plants/places/create/'
    success_message = "%(ar_name)s تم انشائه"

class PlaceListView(generic.ListView):
    model = models.Place
    context_object_name = 'places'
    template_name = "plants/place_list.html"

class PlaceUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.PlaceForm
    model = models.Place

    success_url = '/plants/places/'
    success_message = "%(ar_name)s تم تعديله"

class PlaceDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Place

    success_url = '/plants/places/'
    success_message = "%(ar_name)s تم حذفه"

# Major Views
class Major:
    def major_list(request):
        evaluation_types = models.Major.objects.values('evaluation_type__name', 'evaluation_type__id').distinct()
        majors = models.Major.objects.all()

        return render(request, "plants/major_list.html", {
            'evaluation_types': evaluation_types,
            'majors': majors
        })

class MajorCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.MajorForm
    model = models.Major

    success_url = '/plants/majors/create/'
    success_message = "%(ar_name)s تم انشائه"

# class MajorListView(generic.ListView): 
#     model = models.Major
#     context_object_name = 'majors'
#     template_name = "plants/major_list.html"

class MajorUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.MajorForm
    model = models.Major

    success_url = '/plants/majors/'
    success_message = '%(ar_name)s تم تعديله'

class MajorDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Major

    success_url = '/plants/majors/'
    success_message = "%(ar_name)s تم حذفه"

# Employee Views
class Employee:
    def employee_list(request):
        search_term = request.GET.get('q')
        if search_term:
            employees = models.Employee.objects.filter(Q(ar_name__icontains=search_term) | Q(place__ar_name__icontains=search_term))
        else:
            employees = models.Employee.objects.all()

        return render(request, "plants/employee_list.html", {
            'employees': employees
        })

class EmployeeCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.EmployeeForm
    model = models.Employee

    success_url = "/plants/employees/create/"
    success_message = "%(ar_name)s تم انشائه"

# class EmployeeListView(generic.ListView):
#     context_object_name = 'employees'
#     template_name = "plants/list_employee.html"
#     model = models.Employee

class EmployeeUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.EmployeeForm
    model = models.Employee

    success_url = "/plants/employees/"
    success_message = "%(ar_name)s تم تعديله"

class EmployeeDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Employee

    success_url = '/plants/employees/'
    success_message = "%(ar_name)s تم حذفه"

# Criteria Views

class Criteria:
    def criteria_list(request):
        majors = models.Criteria.objects.values('major__ar_name', 'major__id').distinct() 
        criterias = models.Criteria.objects.all()

        return render(request, "plants/criteria_list.html", {
            'majors': majors,
            'criterias': criterias
        })

class CriteriaCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.CriteriaForm
    model = models.Criteria

    success_url = '/plants/criterias/create/'
    success_message = "%(description)s تم انشائه"

# class CriteriaListView(generic.ListView):
#     context_object_name = 'criterias'
#     model = models.Criteria
#     template_name = 'plants/list_criteria.html'

class CriteriaUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.CriteriaForm
    model = models.Criteria

    success_url = '/plants/criterias/'
    success_message = "%(description)s تم تعديله"

class CriteriaDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Criteria

    success_url = '/plants/criterias/'
    success_message = "%(description)s تم حذفه"

# Evaluation Types
class EvaluationtypeCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.EvaluationTypeForm
    model = models.EvaluationType

    success_url = '/plants/evaluationtypes/create/'
    success_message = "%(name)s تم انشائه"

class EvaluationtypeListView(generic.ListView):
    model = models.EvaluationType
    context_object_name = 'evaluation_types'
    template_name = "plants/evaluation_type_list.html"

class EvaluationtypeUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.EvaluationTypeForm
    model = models.EvaluationType

    success_url = '/plants/evaluationtypes/'
    success_message = "%(name)s تم تعديله"

class EvaluationtypeDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.EvaluationType

    success_url = '/plants/evaluationtypes/'
    success_message = "%(name)s تم حذفه"

class Evaluation:
    def place_detail_evaluationtype(request, pk):
        place = get_object_or_404(models.Place, pk=pk)
        evaluation_types = models.EvaluationType.objects.all()
        return render(request, 'plants/place_detail_evaluationtype.html', {
            'place': place,
            'evaluation_types': evaluation_types
        })

    def place_detail_criteria(request, pk, evaluationtype_pk):
        place = get_object_or_404(models.Place, pk=pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        majors = get_list_or_404(models.Major, evaluation_type=evaluationtype_pk)
        return render(request, 'plants/place_detail_criteria.html', {
            'place': place,
            'evaluation_type': evaluation_type,
            'majors': majors
        })

    def place_detail_employee(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        employees = get_list_or_404(models.Employee, place=place_pk, evaluation_type=evaluationtype_pk)
        if not employees:
            employees = get_list_or_404(models.Employee, place=place_pk)
        return render(request, 'plants/place_detail_employee.html', {
            'place': place,
            'evaluation_type': evaluation_type,
            'major': major,
            'employees': employees
        })

    # basic evaluation View
    def basic_evaluation(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        criterias = get_list_or_404(models.Criteria, major=major_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        employees = models.Employee.objects.filter(place=place_pk, major=major_pk)
        if not employees:
            employees = models.Employee.objects.filter(place=place_pk)

        if request.method == 'POST':
            criteria_list = request.POST.getlist('criteria')
            for i in criteria_list:
                result = models.BasicEvaluation() 
                criteria_instance = models.Criteria.objects.get(pk=i)
                result.criteria = criteria_instance
                employee_pk = request.POST.get('employee_' + i)
                employee_instance = models.Employee.objects.get(pk=employee_pk)
                result.employee = employee_instance
                result.place = place
                result.major = major
                result.yes_or_no = request.POST.get('yes_or_no_' + i)
                result.notes = request.POST.get('notes_' + i)
                result.save()

            messages.add_message(request, messages.SUCCESS, "تم حفظ التقييم")
            return render(request, 'plants/basic_evaluation.html', {
                'place': place,
                'major': major,
                'criterias': criterias,
                'evaluation_type': evaluation_type,
                'employees': employees
            })

        return render(request, 'plants/basic_evaluation.html', {
            'place': place,
            'major': major,
            'criterias': criterias,
            'evaluation_type': evaluation_type,
            'employees': employees
        })

    # Ticket evaluation View
    def ticket_evaluation(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        criterias = get_list_or_404(models.Criteria, major=major_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        employees = models.Employee.objects.filter(place=place_pk)

        if request.method == 'POST':
            criteria_list = request.POST.getlist('criteria')
           
            # if int(answer) == 1:
            #     models.Employee.objects.filter(pk=employee).update(positive_score = F('positive_score') + 1)
            # else:
            #     models.Employee.objects.filter(pk=employee).update(negative_score = F('negative_score') + 1)

            for i in criteria_list: 
                result = models.TicketEvaluation()
                criteria_instance = models.Criteria.objects.get(pk=i)
                result.criteria = criteria_instance
                employee_pk = request.POST.get('employee_' + i)
                employee_instance = models.Employee.objects.get(pk=employee_pk)
                result.employee = employee_instance
                result.place = place
                result.major = major
                result.yes_or_no = request.POST.get('yes_or_no_' + i)
                result.notes = request.POST.get('notes_' + i)
                result.ticket_number = request.POST.get('ticket_number')
                result.save()

            messages.add_message(request, messages.SUCCESS, "تم حفظ التقييم")
            return render(request, 'plants/ticket_evaluation.html', {
                'place': place,
                'major': major,
                'criterias': criterias,
                'evaluation_type': evaluation_type,
                'employees': employees
            })

        return render(request, 'plants/ticket_evaluation.html', {
            'place': place,
            'major': major,
            'criterias': criterias,
            'evaluation_type': evaluation_type,
            'employees': employees
        })

    # Medical Member Evaluation
    def medical_member_evaluation(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        employees = models.Employee.objects.filter(place=place_pk, evaluation_type=evaluationtype_pk)
        if not employees:
            employees = models.Employee.objects.filter(place=place_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        criterias = get_list_or_404(models.Criteria, major=major_pk)

        if request.method == 'POST':
            criteria_list = request.POST.getlist('criteria')
            employee_list = request.POST.getlist('employee')

            for employee in employee_list:
                for criteria in criteria_list:
                    evaluation_value = request.POST.get(criteria + employee)

                    evaluation = models.MemberEvaluation()
                    evaluation.place = place
                    evaluation.major = major
                    criteria_instance = models.Criteria.objects.get(pk=criteria)
                    employee_instance = models.Employee.objects.get(pk=employee)
                    evaluation.criteria = criteria_instance
                    evaluation.employee = employee_instance
                    evaluation.evaluation_score = evaluation_value
                    evaluation.save()

            messages.add_message(request, messages.SUCCESS, 'تم حفظ التقييم')
            return render(request, 'plants/member_evaluation.html', {
                'place': place,
                'major': major,
                'employees': employees,
                'evaluation_type': evaluation_type,
                'criterias': criterias
            })

        return render(request, 'plants/member_evaluation.html', {
            'place': place,
            'major': major,
            'employees': employees,
            'evaluation_type': evaluation_type,
            'criterias': criterias
        })

    # Survey Evaluation
    def survey_evaluation(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        criterias = get_list_or_404(models.Criteria, major=major_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)
        employees = models.Employee.objects.filter(place=place_pk)

        if request.method == 'POST':
            criteria_list = request.POST.getlist('criteria')

            for i in criteria_list:
                result = models.SurveyEvaluation()

                criteria_instance = models.Criteria.objects.get(pk=i)
                result.criteria = criteria_instance

                employee_pk = request.POST.get('employee_' + i)
                employee_instance = models.Employee.objects.get(pk=employee_pk)
                result.employee = employee_instance

                result.place = place
                result.major = major
                
                result.notes = request.POST.get('notes_' + i)
                result.voter_name = request.POST.get('voter_name')
                result.voter_age = request.POST.get('voter_age')
                result.evaluation_score = request.POST.get('vote_' + i)

                result.save()

            messages.add_message(request, messages.SUCCESS, "تم حفظ البيان")
            return render(request, 'plants/survey_evaluation.html', {
                'place': place,
                'major': major,
                'criterias': criterias,
                'evaluation_type': evaluation_type,
                'employees': employees
            })

        return render(request, 'plants/survey_evaluation.html', {
            'place': place,
            'major': major,
            'criterias': criterias,
            'evaluation_type': evaluation_type,
            'employees': employees
        })
    
    # Survey Evaluation Print
    def survey_evaluation_print(request, place_pk, evaluationtype_pk, major_pk):
        place = get_object_or_404(models.Place, pk=place_pk)
        major = get_object_or_404(models.Major, pk=major_pk)
        criterias = get_list_or_404(models.Criteria, major=major_pk)
        evaluation_type = get_object_or_404(models.EvaluationType, pk=evaluationtype_pk)

        return render(request, 'plants/survey_evaluation_print.html', {
            'place': place,
            'major': major,
            'criterias': criterias,
            'evaluation_type': evaluation_type,
        })

class EvaluationView:
    # Reports View
    def reports(request):
        places = models.Place.objects.all()
        evaluation_types = models.EvaluationType.objects.all()
        majors = models.Major.objects.all()
        return render(request, 'plants/report_form.html', {
            'places': places,
            'evaluation_types': evaluation_types,
            'majors': majors
        })

    # Reports Result View
    def evaluation_result(request):
        place = request.GET.get('place')
        evaluation_type = request.GET.get('evaluation_type')
        major = request.GET.get('major')
        fdate = request.GET.get('fdate')
        tdate = request.GET.get('tdate')

        if evaluation_type == 'be':
            results = models.BasicEvaluation.objects.filter(place=place, date__range=(fdate,tdate))
            majors = models.BasicEvaluation.objects.values(
                'major__ar_name', 'major__id'
                ).filter(
                    place=place, date__range=(fdate,tdate)
                ).distinct().annotate(
                    total_positive=Count('yes_or_no', filter=Q(yes_or_no=1))
                ).annotate(
                    total_negative=Count('yes_or_no', filter=Q(yes_or_no=0)
                )
            )

            negatives = models.BasicEvaluation.objects.filter(
                place=place,
                date__range=(fdate,tdate),
                yes_or_no = 0
                )

            major_ar_name = []
            major_total_positive = []
            major_total_negative = []
            for dict_item in majors:
                for key, value in dict_item.items():
                    print(key, value)
                    if key == 'major__ar_name':
                        major_ar_name.append(value)
                    if key == 'total_positive':
                        major_total_positive.append(value)
                    if key == 'total_negative':
                        major_total_negative.append(value)

            custom_style = Style(background='transparent')

            line_chart = pygal.Bar(x_label_rotation=-90,
                                # truncate_label=-1,
                                js=[],
                                show_legend=False,
                                print_values=True,
                                human_readable = True,
                                fill=True,
                                style=custom_style,
                                x_title='المعيار',
                                y_title='التقييم'
                            )

            line_chart.title = 'مخطط توضيحي للنتيجة التحليلة (الايجابيات والسلبيات) للمعايير'
            line_chart.x_labels = major_ar_name

            line_chart.add('الايجابيات', [ 
                {'value': major_total_positive, 'style': 'fill: None; stroke: black; stroke-width: 3'} for major_total_positive in major_total_positive
            ])

            line_chart.add('السلبيات', [ 
                {'value': major_total_negative, 'style': 'fill: None; stroke: black; stroke-width: 3; stroke-dasharray: 15, 10, 5, 10, 15'} for major_total_negative in major_total_negative
            ])

            line_chart.render_to_file('static/charts/be_graph.svg')

            return render(request, 'plants/basic_evaluation_result.html', {
                'results': results,
                'majors': majors,
                'negatives': negatives
            })
        elif evaluation_type == 'mme':
            results = models.MemberEvaluation.objects.filter(place=place, date__range=(fdate,tdate)
                )
            criterias = models.MemberEvaluation.objects.values(
                    'criteria__description', 'major__id', 'criteria__pk'
                ).filter(place=place, date__range=(fdate,tdate)
                ).distinct()
            majors = models.MemberEvaluation.objects.values(
                    'major__ar_name', 'major__id'
                ).filter(
                    place=place, date__range=(fdate,tdate)
                ).distinct()
            employees_scores = models.MemberEvaluation.objects.values(
                'employee__ar_name', 'employee__id',
                ).filter(
                    place=place, date__range=(fdate,tdate)
                ).distinct().annotate(
                    total=Sum('evaluation_score')
                )
            employees_names = models.MemberEvaluation.objects.values(
                'employee__id','employee__ar_name'
                ).filter(
                    place=place, date__range=(fdate,tdate)
                ).distinct()


            employee_names = []
            employee_scores = []
            for employee_name in employees_names:
                for employee_score in employees_scores:
                    if (employee_name['employee__id'] == employee_score['employee__id']):
                        employee_names.append(employee_name['employee__ar_name'])
                        employee_scores.append(employee_score['total'])


            custom_style = Style(background='transparent')

            line_chart = pygal.Bar(x_label_rotation=-90,
                                # truncate_label=-1,
                                js=[],
                                show_legend=False,
                                print_values=True,
                                human_readable = True,
                                fill=True,
                                style=custom_style,
                                x_title='العضو',
                                y_title='التقييم'
                            )

            line_chart.title = 'مخطط توضيحي لنتيجة تقييم اعضاء الفريق الطبي'
            line_chart.x_labels = employee_names
            line_chart.add('التقييم', [ 
                {'value': employee_scores, 'style': 'fill: None; stroke: black; stroke-width: 3'} for employee_scores in employee_scores
            ])

            line_chart.render_to_file('static/charts/me_graph.svg')


            return render(request, 'plants/member_evaluation_result.html', {
                'results': results,
                'criterias': criterias,
                'majors': majors,
                'employees_names': employees_names,
                'employee_scores': employee_scores
            })

        elif evaluation_type == 'te':
            if not major:
                major = 0
            tickets = models.TicketEvaluation.objects.values(
                    'ticket_number'
                ).filter(
                place=place, major=major, date__range=(fdate,tdate)
                ).distinct()

            results = models.TicketEvaluation.objects.filter(
                place=place, major=major, date__range=(fdate,tdate)
                )

            criterias = models.TicketEvaluation.objects.values(
                    'criteria__description', 'criteria__pk'
                ).filter(place=place, major=major, date__range=(fdate,tdate)
                ).distinct().order_by('criteria__pk').annotate(total_error=Cast(Count('yes_or_no', filter=Q(yes_or_no=0)) / float(len(tickets)) * 100, FloatField()))

            errors = models.TicketEvaluation.objects.values(
                    'criteria__pk', 'employee__pk'
                ).filter(place=place, major=major, date__range=(fdate,tdate)
                ).distinct().annotate(error_count=Cast(Count('yes_or_no', filter=Q(yes_or_no=0)) / float(len(tickets)) * 100, FloatField()))

            employees = models.TicketEvaluation.objects.values(
                'employee__ar_name', 'employee__pk'
            ).filter(
                place=place, major=major, date__range=(fdate,tdate)
            ).distinct()

            total_error_plot = []
            criteria_description_plot = []
            for criteria in criterias:
                total_error_plot.append(int(criteria['total_error']))
                criteria_description_plot.append(criteria['criteria__description'])


            custom_style = Style(background='transparent')

            line_chart = pygal.Bar(x_label_rotation=-90,
                                # truncate_label=-1,
                                js=[],
                                show_legend=False,
                                print_values=True,
                                human_readable = True,
                                fill=True,
                                style=custom_style,
                                x_title='المعيار',
                                y_title='نسبة الخطأ'
                            )

            line_chart.title = 'مخطط توضيحي لنتيجة مراجعة التذكرة الطبية'
            line_chart.x_labels = criteria_description_plot
            line_chart.add('% الخطأ', [ 
                {'value': total_error_plot, 'style': 'fill: None; stroke: black; stroke-width: 3'} for total_error_plot in total_error_plot
            ])

            line_chart.render_to_file('static/charts/ticket_graph.svg')


            return render(request, 'plants/ticket_evaluation_result.html', {
                'tickets': tickets,
                'results': results,
                'criterias': criterias,
                'employees': employees,
                'errors': errors,
            })
        
        elif evaluation_type == 'survey':
            voters = models.SurveyEvaluation.objects.values(
                    'voter_name', 'voter_age'
                ).filter(
                place=place, date__range=(fdate,tdate)
                ).distinct()

            results = models.SurveyEvaluation.objects.filter(
                place=place, date__range=(fdate,tdate)
                )

            criterias = models.SurveyEvaluation.objects.values(
                    'criteria__description', 'criteria__pk'
                ).filter(place=place, date__range=(fdate,tdate)
                ).distinct().order_by('criteria__pk').annotate(
                    total=Cast(
                        Sum('evaluation_score') / float(len(voters) * 5) * 100, FloatField()
                    )
                )
            
            total_plot = []
            criteria_description_plot = []
            for criteria in criterias:
                total_plot.append(int(criteria['total']))
                criteria_description_plot.append(criteria['criteria__description'])

            custom_style = Style(background='transparent')

            line_chart = pygal.Bar(x_label_rotation=-90,
                                # truncate_label=-1,
                                js=[],
                                show_legend=False,
                                print_values=True,
                                human_readable = True,
                                fill=True,
                                style=custom_style,
                                x_title='المعيار',
                                y_title='التقييم'
                            )
            line_chart.title = 'مخطط توضيحي لنتيجة استطلاع آراء المنتفعين'
            line_chart.x_labels = criteria_description_plot
            line_chart.add('% النسبة', [ 
                {'value': total_plot, 'style': 'fill: None; stroke: black; stroke-width: 3'} for total_plot in total_plot
            ])

            line_chart.render_to_file('static/charts/survey_graph.svg')

            return render(request, 'plants/survey_evaluation_result.html', {
                'voters': voters,
                'results': results,
                'criterias': criterias,
            })


    # Basic Evaluation Edit
    def basic_evaluation_edit(request, pk):
        basic_evaluation_obj = get_object_or_404(models.BasicEvaluation, pk=pk)
        employees = models.Employee.objects.filter(place=basic_evaluation_obj.place.pk, major=basic_evaluation_obj.major.pk)
        if not employees:
            employees = models.Employee.objects.filter(place=basic_evaluation_obj.place.pk)
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']

        form = forms.BasicEvaluationEditForm()

        if request.method == 'POST':
            form = forms.BasicEvaluationEditForm(instance=basic_evaluation_obj, data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"تم حفظ التعديلات")
                return HttpResponseRedirect(next)

        return render(request, 'plants/basic_evaluation_edit.html', {
            'basic_evaluation_obj': basic_evaluation_obj,
            'employees': employees,
        })


    # Member Evaluation Edit
    def member_evaluation_edit(request, pk):
        member_evaluation_obj = get_object_or_404(models.MemberEvaluation, pk=pk)
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']

        form = forms.MemberEvaluationEditForm()

        if request.method == 'POST':
            form = forms.MemberEvaluationEditForm(instance=member_evaluation_obj, data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"تم حفظ التعديلات")
                return HttpResponseRedirect(next)

        return render(request, 'plants/member_evaluation_edit.html', {
            'member_evaluation_obj': member_evaluation_obj
        })

    # Ticket Evaluation Edit
    def ticket_evaluation_edit(request, pk):
        ticket_evaluation_obj = get_object_or_404(models.TicketEvaluation, pk=pk)
        employees = models.Employee.objects.filter(place=ticket_evaluation_obj.place.pk)
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']

        form = forms.TicketEvaluationEditForm()

        if request.method == 'POST':
            form = forms.TicketEvaluationEditForm(instance=ticket_evaluation_obj, data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"تم التعديل")
                return HttpResponseRedirect(next)

        return render(request, 'plants/ticket_evaluation_edit.html', {
            'ticket_evaluation_obj': ticket_evaluation_obj,
            'employees': employees,
        })

    # Survey Evaluation Edit
    def survey_evaluation_edit(request, pk):
        survey_evaluation_obj = get_object_or_404(models.SurveyEvaluation, pk=pk)
        employees = models.Employee.objects.filter(place=survey_evaluation_obj.place.pk)
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']

        form = forms.SurveyEvaluationEditForm()

        if request.method == 'POST':
            
            form = forms.SurveyEvaluationEditForm(instance=survey_evaluation_obj, data=request.POST)
            if form.is_valid():
                print("Posted!")
                form.save()
                messages.add_message(request, messages.SUCCESS,"تم التعديل")
                return HttpResponseRedirect(next)

        return render(request, 'plants/survey_evaluation_edit.html', {
            'survey_evaluation_obj': survey_evaluation_obj,
            'employees': employees,
        })


    def delete_interval(request):    
        if request.method == 'POST':
            evaluation_type = request.POST.get("evaluation_type")
            fdate = request.POST.get("fdate")
            tdate = request.POST.get("tdate")
            place = request.POST.get("place")
            major = request.POST.get("major")
            if evaluation_type == 'be':
                models.BasicEvaluation.objects.filter(place=place, date__range=(fdate,tdate)).delete()
            elif evaluation_type == 'mme':
                models.MemberEvaluation.objects.filter(place=place, date__range=(fdate,tdate)).delete()
            elif evaluation_type == 'te':
                models.TicketEvaluation.objects.filter(place=place, major=major, date__range=(fdate,tdate)).delete()
            elif evaluation_type == 'survey':
                models.SurveyEvaluation.objects.filter(place=place, date__range=(fdate,tdate)).delete()
            else:
                pass

            messages.add_message(request, messages.SUCCESS, "تم حذف الفترة")
            return HttpResponseRedirect(reverse('plants:get_report'));

        return render(request, 'plants/interval_confirm_delete.html')
    
    def delete_member_evaluation_major(request, major):
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']
        if request.method == 'POST':
            fdate = request.GET.get('fdate')
            tdate = request.GET.get('tdate')
            place = request.GET.get('place')

            models.MemberEvaluation.objects.filter(place=place, major=major, date__range=(fdate,tdate)).delete()
            messages.add_message(request, messages.SUCCESS, "تم حذف التقييم")
            return HttpResponseRedirect(next)

        return render(request, 'plants/member_major_confirm_delete.html', { 'major': major })
    
    def delete_basic_evaluation_major(request, major):
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']
        if request.method == 'POST':
            fdate = request.GET.get('fdate')
            tdate = request.GET.get('tdate')
            place = request.GET.get('place')

            models.BasicEvaluation.objects.filter(place=place, major=major, date__range=(fdate,tdate)).delete()
            messages.add_message(request, messages.SUCCESS, "تم حذف التقييم")
            return HttpResponseRedirect(next)

        return render(request, 'plants/basic_major_confirm_delete.html', { 'major': major })

    def delete_ticket(request, ticket):
        next = "/plants/reports/results/?" + request.META['QUERY_STRING']
        if request.method == 'POST':
            models.TicketEvaluation.objects.filter(ticket_number=ticket).delete()
            messages.add_message(request, messages.SUCCESS, "تم حذف التذكرة")
            return HttpResponseRedirect(next)

        return render(request, "plants/ticket_confirm_delete.html", { 'ticket': ticket })
    
    def delete_survey(request):
        if request.method == 'POST':
            place = request.GET.get('place')
            voter_name = request.GET.get('voter')
            fdate = request.GET.get('fdate')
            tdate = request.GET.get('tdate')
            next = "/plants/reports/results/?" + request.META['QUERY_STRING']
            models.SurveyEvaluation.objects.filter(place=place, voter_name=voter_name, date__range=(fdate, tdate)).delete()
            messages.add_message(request, messages.SUCCESS, "تم حذف الاستطلاع")
            return HttpResponseRedirect(next)
        return render(request, "plants/survey_confirm_delete.html") 


class BasicEvaluationDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.BasicEvaluation

    success_url = '/plants/reports/'
    success_message = 'تم حذف البيان'

class MemberEvaluationDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.MemberEvaluation

    success_url = '/plants/reports/'
    success_message = 'تم حذف البيان'

class TicketEvaluationDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.TicketEvaluation

    success_url = '/plants/reports/'
    success_message = 'تم حذف البيان'

# Ajax Requests
# Get Majors when evaluation types change
def get_majors(request):
    if request.method == 'POST':
        evaluation_type = request.POST.get('evaluation_type')
        if evaluation_type:
            evaluation_type_instance = models.EvaluationType.objects.get(code=evaluation_type)
            majors = models.Major.objects.filter(evaluation_type=evaluation_type_instance)

            data = serializers.serialize("json", majors)
            return HttpResponse(data, content_type='application/json')
        return HttpResponse()