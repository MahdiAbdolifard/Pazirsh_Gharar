from django import forms
from .models import *
from django.forms.widgets import TextInput

class CreateForm(forms.Form):
    fname = forms.CharField(label='نام', widget=forms.TextInput(attrs={ 'placeholder':'مهدی' }))


    lname = forms.CharField(label='نام خانوادگی',required=True, 
                            widget=forms.TextInput(attrs={ 'placeholder':'رضایی' }))


    school_choices = [("اندیشه‌ صفا", "اندیشه‌ صفا"), ("چیتچیان", "چیتچیان"),
                      ("ارشاد", "ارشاد"), ("متفرقه", "متفرقه")]
    school_name = forms.ChoiceField(label='مدرسه', choices=school_choices, required=True)
    custom_school_name = forms.CharField(label='', required=False, 
                                         widget=forms.TextInput(attrs={'placeholder':'09123456789' }))

    def clean(self):
        cleaned_data = super().clean()
        school_name = cleaned_data.get('school_name')

        if school_name == 'متفرقه':
            custom_school_name = cleaned_data.get('custom_school_name')
            if not custom_school_name:
                raise forms.ValidationError('لطفاً نام مدرسه متفرقه را وارد کنید.')

            cleaned_data['school_name'] = custom_school_name



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['custom_school_name'].widget = TextInput(attrs={'style': 'display:none;'})

        if 'school_name' in self.data and self.data['school_name'] != 'متفرقه':
            self.fields['custom_school_name'].widget.attrs.update({'style': 'display:none;'})

        elif 'school_name' in self.data and self.data['school_name'] == 'متفرقه':
            self.fields['custom_school_name'].widget.attrs.update({'style': 'display'})


    phone = forms.CharField(label='شماره تلفن',required=False, max_length=11, min_length=11,
                             widget=forms.TextInput(attrs={'placeholder':'09123456789' }))
    

    parent_phone = forms.CharField(label='شماره تلفن اولیا',required=True, max_length=11, min_length=11,
                             widget=forms.TextInput(attrs={'placeholder':'09123456789' }))


    grade = forms.ChoiceField(label='پایه',choices=[("هفتم", "هفتم"),
                                         ("هشتم", "هشتم"),
                                         ("نهم", "نهم"),],
                                         required=True)


    group_name = forms.ChoiceField(
        label='اسم گروه',
        choices=[
            ("عمار", "عمار"),
            ("مالک اشتر", "مالک اشتر"),
            ("ابوطالب", "ابوطالب"),
            ("جابر", "جابر"),
            ("کمیل", "کمیل"),
            ("حبیب", "حبیب"),
            ("حمزه", "حمزه"),
            ("حنیف", "حنیف"),
            ("مقداد", "مقداد"),
            ("مسلم", "مسلم"),
            ("قیس", "قیس"),                                   
            ("سلمان", "سلمان"),
            ("اویس", "اویس"),
            ("ابوذر", "ابوذر"),
        ],
        required=True,
    )

    def clean_group_name(self):
        group_name = self.cleaned_data.get('group_name')

        if group_name == group_name:
            amar_count = Paziresh.objects.filter(group_name=group_name).count()
            if amar_count >= 5:
                raise forms.ValidationError(f"ظرفیت گروه {group_name} پر شده است.")

        return group_name
        
    created_by = forms.CharField(label='ثبت کننده', required=True,
                             widget=forms.TextInput(attrs={'placeholder':'علیرضا هادی' }))

