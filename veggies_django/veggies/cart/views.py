from django.shortcuts import render
import json
# from flask import jsonify
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader #to load templates
from .models import Veggie#class from models in same folder
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt#to exempt csrf token
def home(request):#get function
  username=request.GET.get('username')
  password=request.GET.get('password')
  if not request.GET.get('username') and not request.GET.get('password'):
     username='username'
     password='password'
  key=username+password
  redis_cache = caches['default']
  redis_client = redis_cache.client.get_client()
  offset=0
  limit=30
  order='id'
  if request.GET.get('orderfield') is not None:
      if request.GET.get('orderby')=='DES':
          order='-'+str(request.GET.get('orderfield'))
      else:
          order=str(request.GET.get('orderfield'))
  if request.GET.get('page') is not None:
      offset=(int(request.GET.get('page'))-1)*int(request.GET.get('pagesize'))
  if request.GET.get('pagesize') is not None:
      limit=int(request.GET.get('pagesize'))+offset
  mymembers = list(Veggie.objects.all().order_by(order)[offset:limit].values())
  dict={}
  for x in mymembers:
      x['quantity']=0
      dict[x['name']]=x
  name=(redis_client.hkeys(key))
  for x in name:
      try:
          dict[x.decode()]['quantity']=(redis_client.hget(key, x.decode())).decode()
      except:
          pass
  a=list(dict.values())#needed this because dict are not json seriazable so mut be passed to list class before it
  return JsonResponse(a,safe=False) # to return as json response


import json
from django.shortcuts import render
from django.core.cache import caches


#using hash table thimngs are done
@csrf_exempt
def cache_create(request):#it will act also as updating the key
    # Get Session Key
    username=request.GET.get('username')
    password=request.GET.get('password')
    if not request.GET.get('username') and not request.GET.get('password'):
        username='username'
        password='password'
    key=username+password
    x=json.loads(request.body)
    redis_cache = caches['default']
    redis_client = redis_cache.client.get_client()

    # String
    redis_client.hset(key, 'name', 'quantity')
   

    # Dictionary
    redis_client.hset(key, x['name'], x['quantity'])
    output_val = (redis_client.hget(key, x['name'])) 
    
    return JsonResponse({'value':{x['name']:(output_val).decode()},'msg':'created'})#decode is to convert byte data to str data
    #https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/


@csrf_exempt
def cache_read(request):
    # Get Session Key
    username=request.GET.get('username')
    password=request.GET.get('password')
    if not request.GET.get('username') and not request.GET.get('password'):
        username='username'
        password='password'
    key=username+password
    redis_cache = caches['default']
    redis_client = redis_cache.client.get_client()
    name=(redis_client.hkeys(key))
    output_val={}
    for x in name:
        try:
            b=list(Veggie.objects.filter(name=x.decode()).values())
            output_val[x.decode()]=b[0]
            output_val[x.decode()]['quantity']=(redis_client.hget(key, x.decode())).decode()
        except:
             pass
    if output_val:
      a=list(output_val.values())
      return JsonResponse(a,safe=False)#decode is to convert byte data to str data
    return JsonResponse({'msg':'novalue'})
  #https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/


@csrf_exempt
def cache_delete(request):
    # Get Session Key
    username=request.GET.get('username')
    password=request.GET.get('password')
    if not request.GET.get('username') and not request.GET.get('password'):
        username='username'
        password='password'
    key=username+password
    x=json.loads(request.body)
    redis_cache = caches['default']
    redis_client = redis_cache.client.get_client()
    redis_client.hdel(key, x['name'])
    return JsonResponse({'msg':'deleted'})
  #https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/

