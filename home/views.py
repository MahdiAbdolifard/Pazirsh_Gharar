from django.shortcuts import render, redirect
from django.contrib import messages
import time


from .models import Paziresh
from .forms import CreateForm
from .send import *


def all(request):
    all = Paziresh.objects.all()
    all_count = Paziresh.objects.all().count()
    return render(request, 'hello.html', {'all_student':all, 'count':all_count})


def group(request):

    malek = Paziresh.objects.all().filter(group_name='مالک اشتر')
    malek_count = Paziresh.objects.all().filter(group_name='مالک اشتر').count()

    amar = Paziresh.objects.all().filter(group_name='عمار')
    amar_count = Paziresh.objects.all().filter(group_name='عمار').count()

    salman = Paziresh.objects.all().filter(group_name='سلمان')
    salman_count = Paziresh.objects.all().filter(group_name='سلمان').count()

    abotaleb = Paziresh.objects.all().filter(group_name='ابوطالب')
    abotaleb_count = Paziresh.objects.all().filter(group_name='ابوطالب').count()

    jaber = Paziresh.objects.all().filter(group_name='جابر')
    jaber_count = Paziresh.objects.all().filter(group_name='جابر').count()

    komal = Paziresh.objects.all().filter(group_name='کمیل')
    komal_count = Paziresh.objects.all().filter(group_name='کمیل').count()

    habib = Paziresh.objects.all().filter(group_name='حبیب')
    habib_count = Paziresh.objects.all().filter(group_name='حبیب').count()

    hamze = Paziresh.objects.all().filter(group_name='حمزه')
    hamze_count = Paziresh.objects.all().filter(group_name='حمزه').count()

    hanif = Paziresh.objects.all().filter(group_name='حنیف')
    hanif_count = Paziresh.objects.all().filter(group_name='حنیف').count()

    meghdad = Paziresh.objects.all().filter(group_name='مقداد')
    meghdad_count = Paziresh.objects.all().filter(group_name='مقداد').count()

    moslem = Paziresh.objects.all().filter(group_name='مسلم')
    moslem_count = Paziresh.objects.all().filter(group_name='مسلم').count()

    ghais = Paziresh.objects.all().filter(group_name='قیس')
    ghais_count = Paziresh.objects.all().filter(group_name='قیس').count()

    ovas = Paziresh.objects.all().filter(group_name='اویس')
    ovas_count = Paziresh.objects.all().filter(group_name='اویس').count()

    abozar = Paziresh.objects.all().filter(group_name='ابوذر')
    abozar_count = Paziresh.objects.all().filter(group_name='ابوذر').count()

    return render(request, 'group.html', {'malek':malek, 'malek_count':malek_count,
                                          'amar':amar, 'amar_count':amar_count,
                                          'abotaleb':abotaleb, 'abotaleb_count':abotaleb_count,
                                          'jaber':jaber, 'jaber_count':jaber_count,
                                          'komal':komal, 'komal_count':komal_count,
                                          'habib':habib, 'habib_count':habib_count,
                                          'hamze':hamze, 'hamze_count':hamze_count,
                                          'hanif':hanif, 'hanif_count':hanif_count,
                                          'meghdad':meghdad, 'meghdad_count':meghdad_count,
                                          'moslem':moslem, 'moslem_count':moslem_count,
                                          'ghais':ghais, 'ghais_count':ghais_count,
                                          'ovas':ovas, 'ovas_count':ovas_count,
                                          'abozar':abozar, 'abozar_count':abozar_count,
                                          'salman':salman, 'salman_count':salman_count,})



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
    d_count = Paziresh.objects.all().filter(school_name="امام عصر").count()
    z_count = all - (a_count + b_count + c_count + d_count)

    return render(request, 'school.html', {'count':all, '1_count':a_count, '2_count':b_count,
                                           '4_count':d_count, 
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
            # send(cd['phone']) 
            # test_send(cd['phone'])
# -------------------------------------------------------------
            # send(request ,cd['phone'])
            # send(request, cd['parent_phone'])
# -------------------------------------------------------------
            # send_child(cd['phone'], cd['fname'])
            # send_parent(cd['parent_phone'], cd['lname'])

            time.sleep(3)
            messages.success(request, 'پیام‌‌ها با موفقیت ارسال شد', 'primary')
            time.sleep(1)
            return redirect('allstudent')
            
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form':form})


def test(request):
    return render(request, 'test.html')