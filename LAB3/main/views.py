from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    date1 = datetime.now()
    response = {'date': str(date1), 'current_page': request.build_absolute_uri(), 'server_info': os.uname().sysname , 'client_info': os.getlogin()}
    return JsonResponse(response)
