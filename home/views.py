import datetime
from multiprocessing import connection

from django.shortcuts import render
from django.db.models import Count
from django.db.models import F
from django.db.models import Q
from .models import *


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


def fanlarga_birikishview(request):
    #
    # context = {
    #     "year_list1": EEducationYear.objects.all().order_by('code'),
    #     "fan_list": ECurriculumSubject.objects.filter(field_curriculum__active=True).values('field_semester').annotate(
    #     count=Count('field_semester')).order_by('field_semester'),
    #     "fakultet_list1": EDepartment.objects.filter(field_structure_type=11).filter(~Q(id__in=[7, 8, 76, 77])),
    #     "fanga_birikish": EStudentMeta.objects.filter(field_student_status=11, active=True, ).order_by('field_department__name', 'field_education_year__name').filter(
    #     ~Q(field_department__in=[7, 8, 77]))[:20],
    # }

    queryset = (
        HSemestr.objects
        .select_related('field_curriculum__field_education_year', 'field_curriculum__field_department','field_curriculum__curriculum_subject')
        .filter(field_curriculum__field_education_form='11', field_education_year='2023',field_curriculum__field_department='2')
        .order_by('field_curriculum__field_education_year', 'field_curriculum__name')
        .values('field_curriculum__field_department__name', 'field_curriculum__field_education_year',
                'field_curriculum__field_education_year__name', 'field_education_year', 'name', 'field_curriculum__name')
        .select_related('field_curriculum__field_department', 'field_curriculum__field_education_year')
        .filter(field_curriculum__field_education_form='11', field_curriculum__field_education_year='2023',
                field_curriculum__field_department_id='2')
        .order_by('field_curriculum__field_education_year')
        .values('field_curriculum__field_department__name', 'field_curriculum__field_education_year',
                'field_curriculum__field_education_year__name', 'field_education_year', 'name')
        .distinct()
    )

    context = {
        'queryset': queryset
    }

    return render(request, "fanlarga_birikish.html", context)


def oquv_yiliview(request):
    code = 11
    h = HSemestr.objects.filter(field_education_year=oquv_yiliview()[0][0],
                                code__in=[f"{10 + i}" for i in range(11, 11, 2)])
    cur_ids = []
    for i in h:
        cur_ids.append(i.field_curriculum_id)

    student_list = EStudentMeta.objects.filter(field_student_status=11, active=True,
                                               field_curriculum__in=cur_ids).values('field_department__name',
                                                                                    'field_education_year__name').annotate(
        count=Count('field_department__name')).order_by('field_department__name', 'field_education_year__name').filter(
        ~Q(field_department_id__in=[7, 8, 77, 6]))

    year_list = EStudentMeta.objects.filter(field_student_status=11, active=True).values(
        'field_education_year__name').annotate(count=Count('id')).filter(
        ~Q(field_department_id__in=[7, 8, 77, 6]))
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
        a = i[1] + i[2] + i[3] + i[4]
        data[cnt].append(a)
        data[cnt].append((i[3] / a * 100))
        sum_foiz += (i[3] / a * 100) / len(data)
        b = "%.2f" % ((i[3] / a * 100))
        data[cnt].append(b)
        sum_foiz += float(b)
        cnt += 1
    # for i in data:
    #     print(i)

    context = {

        "year_list": year_list,
        'data': data,
        'sum_year_list': sum_year_list,
        'sum_foiz': sum_foiz
        # "department": EDepartment.objects.filter(field_structure_type=11).filter(~Q(id__in=[7, 8, 76, 77])),
        'sum_foiz': sum_foiz / len(data)
    }

    return render(request, "oquv_yili.html", context)
