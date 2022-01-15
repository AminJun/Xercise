from datetime import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView


class HamidVU(TemplateView):
    template_name = 'hamids.html'

class AminVU(TemplateView):
    template_name = 'amin.html'
