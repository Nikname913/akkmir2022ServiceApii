from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import xml.etree.ElementTree as ET 
import requests
import xmltodict 
import json 
import os

# ------------------------------
# file = open(pwd + '/static/data/test.xml')
# ------------------------------

pwd = os.path.dirname(__file__)

@csrf_exempt
def writeXmlData(request):

  if request.method == 'POST':

    xml = request.body

    jsonParse = xmltodict.parse(xml)
    jsonText = json.dumps(jsonParse)

    file = open(pwd + '/static/data/warehouses.json', 'w')
    file.write(jsonText)
    file.close() 

    return HttpResponse(200)

def getUslugiList(request):

  file = open(pwd + '/static/data/services.json')
  content = file.read()
  file.close()

  return HttpResponse(content)

def getServicesList(request):

  file = open(pwd + '/static/data/warehouses.json')
  content = file.read()
  file.close()

  return HttpResponse(content)

def getServicesListOne(request):

  if request.method == 'POST':

    file = open(pwd + '/static/data/warehouses.json')
    content = file.read()
    file.close()

    return HttpResponse(content)

@csrf_exempt
def newWriting(request):

  if request.method == 'POST':

    reqData = request.body
    reqDataDeserialize = json.loads(reqData)
    writingsList = open(pwd + '/static/data/writings.json')
    content = writingsList.read()
    writingsList.close()
    writingsListDeserialize = json.loads(content)

    writingsListDeserialize['data'].append(reqDataDeserialize)
    newWritingList = json.dumps(writingsListDeserialize)

    # валидация будет происходить на клиенте
    # в момент формирования пакета заявки и перед
    # отправкой его непосредственно на сервер

    writingsList = open(pwd + '/static/data/writings.json', 'w')
    writingsList.write(newWritingList)
    writingsList.close()

    service  = reqDataDeserialize['service']
    user     = reqDataDeserialize['user']
    number   = reqDataDeserialize['number']
    date     = reqDataDeserialize['date']
    time     = reqDataDeserialize['time']
    workType = reqDataDeserialize['workType']

    pack = dict()

    pack['client'] = user
    pack['number'] = number
    pack['time'] = date + ' ** ' + time
    pack['workType'] = workType
    pack['service'] = service

    tCHAT = '-614796063'
    tNik = '789039165'
    tMasha = '2057594093'
    
    USERS = [ tCHAT, tNik, tMasha ]
    USER = USERS[1]
    ABOUT = 'Пользователь: ' + user + '. ID сервисцетра: ' + service + '. Номер: ' + number + '. Проводимые работы: ' + workType + '. Время: ' + date + ' ** ' + time
    URL = "https://api.telegram.org/bot5576870672:AAFR3ZYE4UtbjD1WVd3L6Zy2j0thCCz5pPk/sendMessage?chat_id=" + USER + "&text=" + ABOUT
    
    req = requests.get(URL)
    return HttpResponse(req.status_code)

def getWritingsList(request):

  file = open(pwd + '/static/data/writings.json')
  content = file.read()
  file.close()

  return HttpResponse(content)
        
def pingMethod(request):

  jsonClients = ''

  xmlTestParse = ET.parse(pwd + '/static/data/akkmir.xml')
  xmlTestRoot = xmlTestParse.getroot()

  with open(pwd + '/static/data/akkmir.xml', encoding="utf-8") as fd: 
    
    jsonText = xmltodict.parse(fd.read())
    jsonClients = json.dumps(jsonText)

  for node in xmlTestRoot:

    if node.tag == 'clients':

      clients = node

  return HttpResponse(jsonClients)