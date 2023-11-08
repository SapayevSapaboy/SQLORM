import datetime
from multiprocessing import connection

from django.shortcuts import render
from django.db.models import Count
from .models import EDepartment
from django.db.models import Q
from .models import ECurriculumSubject, EEducationYear, EStudentMeta

# Create your views here.

def homeview(request):
    context = {
        "kafedra_list": EDepartment.objects.filter(field_structure_type=12),
        "fakultet_list": EDepartment.objects.filter(field_structure_type=11).filter(~Q(id__in=[7, 8, 76, 77]))
    }
    return render(request, "index.html", context)


def yonalish_view(request, kafedra_id):
    context = {
        "year_list": EEducationYear.objects.all().order_by('code'),
        "yonalish": ECurriculumSubject.objects.filter(field_department__id=kafedra_id, field_curriculum__active=True),
        'kafedra_id': kafedra_id,
    }
    print(kafedra_id)

    return render(request, "fanlar.html", context)



def fanlarga_birikishview(request,):

    # with connection.cursor() as cursor:
    #     cursor.execute(""" SELECT * FROM e_department WHERE "_structure_type"='11' AND "id" NOT IN (77, 8, 7, 6);""")
    #     faculties_list = cursor.fetchall()
    #     cursor.execute(""" SELECT * FROM h_education_form WHERE code in ('11','13','15','16','17') ORDER BY code ;""")
    #     education_form_list = cursor.fetchall()
    #
    # bugungi_yil = datetime.datetime.now().year
    # entered_year = [{"year": i, "name": f"{i}-{i + 1}"} for i in range(bugungi_yil - 5, bugungi_yil + 1)]
    #
    # context = {
    #     "faculties_list": faculties_list,
    #     "education_form_list": education_form_list,
    #     "entered_year": entered_year,
    #
    # }

    context = {
        "year_list1": EEducationYear.objects.all().order_by('code'),
        "fakultet_list1": EDepartment.objects.filter(field_structure_type=11).filter(~Q(id__in=[7, 8, 76, 77])),
        "fanga_birikish": EStudentMeta.objects.filter(field_student_status=11, active=True, ).order_by('field_department__name', 'field_education_year__name').filter(
        ~Q(field_department__in=[7, 8, 77]))[:20]
    }

    return render(request, "fanlarga_birikish.html", context)



def oquv_yiliview(request):
    student_list = EStudentMeta.objects.filter(field_student_status=11, active=True).values('field_department__name',
                                                                                            'field_education_year__name').annotate(
        count=Count('field_department__name')).order_by('field_department__name', 'field_education_year__name').filter(
        ~Q(field_department__in=[7, 8, 77]))

    year_list = EStudentMeta.objects.filter(field_student_status=11, active=True).values(
        'field_education_year__name').annotate(count=Count('id')).filter(
        ~Q(field_department__in=[7, 8, 77]))
    sum_year_list = 0
    for i in year_list:
        sum_year_list += i['count']

    data = []
    row = []
    cnt = 0
    dep = student_list[0]['field_department__name']
    for i in student_list:
        if dep != i['field_department__name']:
            while len(row) < len(year_list) + 1:
                row.append(0)
            data.append(row)
            row = []
            dep = i['field_department__name']
            cnt = 0

        if len(row) == 0:
            row.append(dep)
        if dep == i['field_department__name']:

            if year_list[cnt]['field_education_year__name'] != i['field_education_year__name']:
                while True:
                    if year_list[cnt]['field_education_year__name'] == i['field_education_year__name']:
                        row.append(i['count'])
                        cnt += 1
                        break
                    else:
                        row.append(0)
                        cnt += 1
            else:

                if year_list[cnt]['field_education_year__name'] == i['field_education_year__name']:
                    row.append(i['count'])
                    cnt += 1
                else:
                    row.append(0)
                    cnt += 1
    while len(row) < len(year_list) + 1:
        row.append(0)
    data.append(row)

    cnt = 0
    sum_foiz = 0
    for i in data:
        a = sum(i[1:6])
        data[cnt].append(a)
        b="%.2f"% ((i[3] / a * 100))
        data[cnt].append(b)
        sum_foiz += float(b)
        cnt += 1

    context = {

        "year_list": year_list,
        'data': data,
        'sum_year_list': sum_year_list,
        'sum_foiz':  sum_foiz/len(data)
    }

    return render(request, "oquv_yili.html", context)