from django import forms

class CreateForm(forms.Form):
    fname = forms.CharField(label='نام')
    lname = forms.CharField(label='نام خانوادگی',required=True)
    school_name = forms.CharField(label='مدرسه',required=True)
    phone = forms.CharField(label='شماره تلفن',required=True)
    grade = forms.ChoiceField(label='پایه',choices=[("هفتم", "هفتم"),
                                         ("هشتم", "هشتم"),
                                         ("نهم", "نهم"),],
                                         required=True)
    created_by = forms.CharField(label='ثبت کننده',required=True)