from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from cvs.models import *

import datetime

user_obj = User.objects.get(user_email="conanchou1412@gmail.com")
theme = Settings.objects.get(user=user_obj).theme + "/"

def index(request):
    """docstring for index"""
    now = datetime.datetime.now()
    t = get_template(theme + 'index.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
