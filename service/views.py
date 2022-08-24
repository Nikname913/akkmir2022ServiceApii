from dataclasses import dataclass
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import xml.etree.ElementTree as ET 
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

    file = open(pwd + '/static/data/akkmir.json', 'w')
    file.write(jsonText)
    file.close() 

    return HttpResponse(200)

def getServicesList(request):

  file = open(pwd + '/static/data/akkmir.json')
  content = file.read()
  file.close()

  return HttpResponse(content)

@csrf_exempt
def newWriting(request):

  # { 'service': 'ef7f622d-b37b-11e9-80ef-00155d0bfb06',
  #   'user': 'Николай Шипов',
  #   'number': '9068085023',
  #   'date': '30-08-2022',
  #   'time': '19:00',
  #   'workType': 'Шиномонтаж',
  #   'auto': 'lada vesta',
  #   'model': 'кто ее знает',
  #   'email': 'nik.shipov@gmail.com',
  #   'comment': 'без комментариев' }

  if request.method == 'POST':

    reqData = request.body
    reqDataDeserialize = json.loads(reqData)
    writingsList = open(pwd + '/static/data/writings.json')
    content = writingsList.read()
    writingsList.close()
    writingsListDeserialize = json.loads(content)

    writingsListDeserialize['data'].append(reqDataDeserialize)
    newWritingList = json.dumps(writingsListDeserialize)

    writingsList = open(pwd + '/static/data/writings.json', 'w')
    writingsList.write(newWritingList)
    writingsList.close()

    service  = reqDataDeserialize['service']
    user     = reqDataDeserialize['user']
    number   = reqDataDeserialize['number']
    date     = reqDataDeserialize['date']
    time     = reqDataDeserialize['time']
    workType = reqDataDeserialize['workType']

    auto     = reqDataDeserialize['auto']
    model    = reqDataDeserialize['model']
    email    = reqDataDeserialize['email']
    comment  = reqDataDeserialize['comment']

    return HttpResponse(200)
        
def exampleMethod(request):

  jsonClients = ''

  xmlTestParse = ET.parse(pwd + '/static/data/akkmir.xml')
  xmlTestRoot = xmlTestParse.getroot()

  with open(pwd + '/static/data/akkmir.xml') as fd: 
    
    jsonText = xmltodict.parse(fd.read())
    jsonClients = json.dumps(jsonText)

  for node in xmlTestRoot:

    if node.tag == 'clients':

      clients = node

  return HttpResponse(jsonClients)