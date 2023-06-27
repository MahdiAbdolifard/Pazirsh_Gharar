from django import forms

class CreateForm(forms.Form):
    fname = forms.CharField(label='نام', widget=forms.TextInput(attrs={ 'placeholder':'مهدی' }))
    lname = forms.CharField(label='نام خانوادگی',required=True, widget=forms.TextInput(attrs={ 'placeholder':'رضایی' }))

    school_name = forms.ChoiceField(label='مدرسه',choices=[("اندیشه‌ صفا", "اندیشه‌ صفا"), ("چیتچیان", "چیتچیان"),
                                         ("ارشاد", "ارشاد"), ("متفرقه", "متفرقه")],
                                         required=True)
    
    phone = forms.CharField(label='شماره تلفن',required=False, max_length=11, min_length=11,
                             widget=forms.TextInput(attrs={'placeholder':'09123456789' }))
    
    parent_phone = forms.CharField(label='شماره تلفن اولیا',required=True, max_length=11, min_length=11,
                             widget=forms.TextInput(attrs={'placeholder':'09123456789' }))

    grade = forms.ChoiceField(label='پایه',choices=[("هفتم", "هفتم"),
                                         ("هشتم", "هشتم"),
                                         ("نهم", "نهم"),],
                                         required=True)
    group_name = forms.ChoiceField(label='اسم گروه',choices=[("عمار", "عمار"),
                                         ("مالک اشتر", "مالک اشتر"),
                                         ("سلمان فارسی", "سلمان فارسی"),],
                                         required=True)
        
    created_by = forms.CharField(label='ثبت کننده', required=True,
                             widget=forms.TextInput(attrs={'placeholder':'علیرضا هادی' }))

