from django.urls import path
from service import views

urlpatterns = [

    # ----------------------------
    # тестовый метод, проверяется в браузере через GET запрос
    # ----------------------------
    path('example', views.exampleMethod, name='example'),
    # ----------------------------
    # этот и далее методы работают через POST и GET запросы
    # метод записи данных их xml файла в базовый json файл
    # ----------------------------
    path('writeXML', views.writeXmlData, name='writeXML'),
    path('getServicesList', views.getServicesList, name='getServicesList'),
    path('newWriting', views.newWriting, name='newWriting')
    
]