from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

import datetime

def index(request):
    """docstring for index"""
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
