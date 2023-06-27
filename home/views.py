from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Paziresh
from .forms import CreateForm
from .send import send



def test(request):
    all = Paziresh.objects.all()
    all_count = Paziresh.objects.all().count()
    return render(request, 'hello.html', {'all_student':all, 'count':all_count})


def group(request):
    malek = Paziresh.objects.all().filter(group_name='مالک اشتر')
    malek_count = Paziresh.objects.all().filter(group_name='مالک اشتر').count()

    amar = Paziresh.objects.all().filter(group_name='عمار')
    amar_count = Paziresh.objects.all().filter(group_name='عمار').count()

    return render(request, 'group.html', {'malek':malek, 'malek_count':malek_count,
                                          'amar':amar, 'amar_count':amar_count,})



def grade(request):
    haftom = Paziresh.objects.all().filter(grade='هفتم')
    haftom_count = Paziresh.objects.all().filter(grade='هفتم').count()

    hashtom = Paziresh.objects.all().filter(grade='هشتم')
    hashtom_count = Paziresh.objects.all().filter(grade='هشتم').count()

    nohom = Paziresh.objects.all().filter(grade='نهم')
    nohem_count = Paziresh.objects.all().filter(grade='نهم').count()

    return render(request, 'grade.html', {'haftom':haftom, 'haftom_count':haftom_count,
                                          'hashtom':hashtom, 'hashtom_count':hashtom_count,
                                          'nohom':nohom, 'nohem_count':nohem_count,})


def school(request):

    all = Paziresh.objects.all().count()
    a_count = Paziresh.objects.all().filter(school_name='اندیشه‌ صفا').count()
    b_count = Paziresh.objects.all().filter(school_name='ارشاد').count()
    c_count = Paziresh.objects.all().filter(school_name='چیتچیان').count()

    z_count = Paziresh.objects.all().filter(school_name='متفرقه').count()

    return render(request, 'school.html', {'count':all, '1_count':a_count, '2_count':b_count,
                                           '3_count':c_count, 'z_count':z_count,})


def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Paziresh.objects.create(fname=cd['fname'], lname=cd['lname'], school_name=cd['school_name'], 
                                    phone=cd['phone'], grade=cd['grade'], created_bey=cd['created_by'],
                                    parent_phone=cd['parent_phone'], group_name=cd['group_name'])
            messages.success(request, 'دانش‌آموز با موفقیت ثبت شد', 'success')
            send(cd['phone'],)
            send(cd['parent_phone'])
            messages.success(request, 'پیام ارسال شد', 'primary')
            return redirect('allstudent')
            
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form':form})
