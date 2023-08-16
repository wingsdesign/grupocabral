from django.db.models import Count, Min, Sum, Avg, Q, Max
from grupocabral.noticias.models import *
from django.template import RequestContext
from datetime import datetime
def grupocabral(request):
    return{
        'base_noticias': Noticia.objects.order_by('-id'),
        'base_noticias_left': Noticia.objects.order_by('-data')[:4],
        'base_noticias_bottom': Noticia.objects.all()[:3],

        }
