from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime
import time


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    date1 = datetime.now()
    response = dict(date= time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), current_page=request.path, server_info=os.name, client_info=os.uname()[1])
    return JsonResponse(response)
