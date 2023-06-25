from django import forms

class CreateForm(forms.Form):
    fname = forms.CharField(label='نام')
    lname = forms.CharField(label='نام خانوادگی',required=True)
    school_name = forms.CharField(label='مدرسه',required=True)
    phone = forms.CharField(label='شماره تلفن',required=True, max_length=11, min_length=11)
    parent_phone = forms.CharField(label='شماره تلفن اولیا',required=True, max_length=11, min_length=11)
    grade = forms.ChoiceField(label='پایه',choices=[("هفتم", "هفتم"),
                                         ("هشتم", "هشتم"),
                                         ("نهم", "نهم"),],
                                         required=True)
    group_name = forms.ChoiceField(label='اسم گروه',choices=[("عمار", "عمار"),
                                         ("مالک اشتر", "مالک اشتر"),
                                         ("سلمان فارسی", "سلمان فارسی"),],
                                         required=True)
        
    created_by = forms.CharField(label='ثبت کننده',required=True)

