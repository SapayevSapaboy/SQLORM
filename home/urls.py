from django.urls import path
from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('oquv_yili/', oquv_yiliview, name='oquv_yili'),
    path('fanlarga_birikish/', fanlarga_birikishview, name='fanlarga_birikish'),
    # path('fanlar/<str:kafedra_id>/',fanlarview, name='fanlarview'),
    path('yonalishlar/<str:kafedra_id>/',yonalish_view, name='yonalishlarview'),
]
