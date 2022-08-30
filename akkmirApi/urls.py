from django.urls import path
from service import views

urlpatterns = [

    # ----------------------------
    # тестовый метод, проверяется в браузере через GET запрос
    # ----------------------------
    path('example', views.pingMethod, name='EXAMPLE'),
    # ----------------------------
    # метод записи данных их xml файла в базовый json файл
    # ----------------------------
    path('writeXML', views.writeXmlData, name='WRITE_XML'),
    # ----------------------------
    # получить список сервис-центров и складов
    # ----------------------------
    path('getServicesList', views.getServicesList, name='GET_SERVICES'),
    # ----------------------------
    # получить список доступных услуг
    # ----------------------------
    path('getUslugiList', views.getUslugiList, name='GET_USLUGI'),
    # ----------------------------
    # получить список всех записей в сц
    # ----------------------------
    path('getWritingsList', views.getWritingsList, name='GET_WRITINGS'),
    # ----------------------------
    # получить информацию об одном сервис центре
    # ----------------------------
    path('getServicesListOne', views.getServicesListOne, name='GET_SERVICE_ONE'),
    # ----------------------------
    # добавить новую запись в один из сервис-центров
    # ----------------------------
    path('newWriting', views.newWriting, name='NEW_WRITING'),
    
]