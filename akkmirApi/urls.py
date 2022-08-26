from django.urls import path
from service import views

urlpatterns = [

    # ----------------------------
    # тестовый метод, проверяется в браузере через GET запрос
    # ----------------------------
    path('example', views.pingMethod, name='EXAMPLE'),
    # ----------------------------
    # этот и далее методы работают через POST и GET запросы
    # метод записи данных их xml файла в базовый json файл
    # ----------------------------
    path('writeXML', views.writeXmlData, name='WRITE_XML'),
    path('getServicesList', views.getServicesList, name='GET_SERVICES'),
    path('getUslugiList', views.getUslugiList, name='GET_USLUGI'),
    path('getWritingsList', views.getWritingsList, name='GET_WRITINGS'),
    path('getServicesListOne', views.getServicesListOne, name='GET_SERVICE_ONE'),
    path('newWriting', views.newWriting, name='NEW_WRITING'),
    
]