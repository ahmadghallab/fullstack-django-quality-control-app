from django import forms
from . import models

class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ['ar_name']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            })
        }

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "الاسم"

class MajorForm(forms.ModelForm):
    class Meta:
        model = models.Major
        fields = ['ar_name','evaluation_type']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            }),
        }
    def __init__(self, *args, **kwargs):
        super(MajorForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "الاسم"
        self.fields['evaluation_type'].label = "نوع التقييم"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['ar_name', 'place', 'major', 'evaluation_type', 'address', 'telephone', 'join_year', 'positive_score', 'negative_score']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            }),
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "الاسم"
        self.fields['place'].label = "جهة العمل"
        self.fields['major'].label = "التخصص"
        self.fields['evaluation_type'].label = "نوع التقييم"
        self.fields['address'].label = "العنوان"
        self.fields['telephone'].label = "التليفون"
        self.fields['join_year'].label = "سنة التعيين"
        self.fields['positive_score'].label = "الايجابيات"
        self.fields['negative_score'].label = "السلبيات"

class CriteriaForm(forms.ModelForm):
    class Meta:
        model = models.Criteria
        fields = ['major', 'description', 'solution', 'limit']
        widgets = {
            'description': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            }),
            'solution': forms.TextInput(attrs={
                'autocomplete': 'off',
            }),
            'limit': forms.NumberInput(attrs={
                'autocomplete': 'off',
            })
        }

    def __init__(self, *args, **kwargs):
        super(CriteriaForm, self).__init__(*args, **kwargs)
        self.fields['major'].label = "التخصص"
        self.fields['description'].label = "المعيار"
        self.fields['solution'].label = "الحل المقترح"
        self.fields['limit'].label = "حد المعيار"

class EvaluationTypeForm(forms.ModelForm):
    class Meta:
        model = models.EvaluationType
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            }),
            'code': forms.TextInput(attrs={
                'autocomplete': 'off',
                'required': 'true'
            })
        }

    def __init__(self, *args, **kwargs):
        super(EvaluationTypeForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "الاسم"
        self.fields['code'].label = "الرمز"

class BasicEvaluationEditForm(forms.ModelForm):
    class Meta:
        model = models.BasicEvaluation
        fields = ['yes_or_no', 'notes', 'employee']

class MemberEvaluationEditForm(forms.ModelForm):
    class Meta:
        model = models.MemberEvaluation
        fields = ['evaluation_score']

class TicketEvaluationEditForm(forms.ModelForm):
    class Meta:
        model = models.TicketEvaluation
        fields = ['yes_or_no', 'employee']

class SurveyEvaluationEditForm(forms.ModelForm):
    class Meta:
        model = models.SurveyEvaluation
        fields = ['evaluation_score', 'employee', 'notes']