from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import initiate_paymet
from . import confirm_varidation
from . import generate_token
def starter(request,*args,**kwargs):
   # confirm_varidation.confirm_varidation()
    print(generate_token.get_token())
    response = initiate_paymet.initiate_payment()
    return JsonResponse({'response':response})


def confirm(request,*args,**kwargs):
    return JsonResponse({'detailis':{
        'args':args,
        'kwargs':kwargs,
        'reqeust':request.GET or request.POST
    }})
def validate(request,*args,**kwargs):
     return JsonResponse({'detailis':{
        'args':args,
        'kwargs':kwargs,
        'reqeust':request.GET or request.POST
    }})