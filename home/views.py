import datetime

from django.shortcuts import render

from .models import EDepartment
from .models import ECirculationSheet
from django.db.models import Q
from .models import ECurriculum, ECurriculumSubject, EEducationYear, HCourse, HSubjectBlock, HSubjectGroup,EStudentMeta


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

def oquv_yiliview(request):
    context = {
        "student_list": EStudentMeta.objects.filter(field_student_status=11,active=True),
     #  "department": EDepartment.objects.filter(field_structure_type=11,estudentmeta__field_student_status=11,estudentmeta__active=True).filter(~Q(id__in=[7, 8, 76, 77])),
    }
    return render(request, "oquv_yili.html", context)


#def dependantfild(request):
 #   yearid = request.GET.get('year', None)
  #  stateid = request.GET.get('state', None)
   # state = None
   # district = None
   # if countryid:
   #     getyear = EEducationYear.objects.get(id= yearid)
   #     state = ECurriculum.objects.get(emp)

# def fanlarview(request,kafedra_id):
#     edu_year_list={}
#     current_year=datetime.datetime.now().year
#     for i in range(2016,current_year+1):
#         edu_year_list.update({f"{i}":f"{i}-{i+1}"})
#
#     context = {
#         "edu_year_list":edu_year_list,
#         "oquvyili": ECirculationSheet.objects.filter(field_department__field_structure_type=11)
#     }
#
#     return render(request, 'fanlar.html',context)
#
