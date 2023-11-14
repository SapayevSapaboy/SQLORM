from django.db import connection

def fanlarga_birikmagan_talabalar(semester, entered_year, kafid):
    with connection.cursor() as cursor:
        cursor.execute(f""" select ed._translations->>'name_uz' as fakultet, ec._translations->>'name_uz' as reja, hs._curriculum, 
                          concat(cast(hs.code as int)-10, '-semestr'), 
                          sum(case when ecs.in_group IS NULL then 1
                                   when ecs.in_group = '' then 1
                                   when cast(ecs.in_group as int) = ecs.id then 1
                          end) as fansoni,
                          sum(case when ecs.in_group IS NULL then ecs.total_acload
                                   when ecs.in_group = '' then ecs.total_acload
                                   when cast(ecs.in_group as int) = ecs.id then ecs.total_acload
                          end) as yuklama,
                          sum(case when ecs.in_group IS NULL then ecs.credit
                                   when ecs.in_group = '' then ecs.credit
                                   when cast(ecs.in_group as int) = ecs.id then ecs.credit
                          end) as creditsoni,
                                  (
                                    select count(esm.id) from e_student_meta esm where esm._semestr = hs.code and esm._curriculum=hs._curriculum and esm._student_status = '11' and esm.active = true
                                  ) as talabasoni,
                                  (
                                    select count(ess.id) from e_student_subject ess where ess._semester = hs.code and ess._curriculum=hs._curriculum 
                                     and ess._education_year = hs._education_year and 
                                    ess._subject IN( select ecs2._subject from e_curriculum_subject ecs2 where ecs2._curriculum = hs._curriculum and ecs2._semester = hs.code and ecs2.active = true) 
                                    and exists (
                                        select 1 from e_student_meta esm2 where esm2._semestr = ess._semester and esm2._curriculum=ess._curriculum 
                                        and esm2._student_status = '11' and esm2.active = true and esm2._student = ess._student
                                         )
                                  ) as fantalaba
                            from h_semestr hs 
                            left join e_curriculum_subject ecs on ecs._curriculum = hs._curriculum and ecs._semester = hs.code and ecs.active = true
                            inner join e_curriculum ec on ec.id = hs._curriculum
                            inner join e_department ed on ed.id = ec._department and ed.id not in ('7', '8', '76', '77')
                            where hs._education_year = '{entered_year}' and cast(hs.code as int) % 2 = {semester}  --and hs._curriculum=853
                            group by hs._curriculum, hs.code,hs._education_year, ec._translations->>'name_uz', ed._translations->>'name_uz'
                            order by ed._translations->>'name_uz', hs.code, ec._translations->>'name_uz';""")

        fan_birikish = cursor.fetchall()

    return fan_birikish


def get_department_name_by_id(id):
    with connection.cursor() as cursor:
        cursor.execute(f""" select name from e_department where id={id};""")
        department_name = cursor.fetchall()
    return department_name
