# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from grupocabral import helpers_pagination
from .models import Filias
from .forms import ComentarioForm

class FilialListView(ListView):
    model = Filias
    template_name = 'filiais.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FilialListView, self).get_context_data(*args, **kwargs)
        lista_filiais = Filias.objects.all()
        lista_filiais = helpers_pagination.pg_records(self.request, lista_filiais, 6)
        context = {
            'lista_filiais': lista_filiais,
            #'paginacao_filiais':paginacao_filiais,
        }
        return context

# class FilialDetalhesView(DetailView):
#     model = Filias
#     context_object_name = 'object_lists'
#     template_name = 'filiais_detalhes.html'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         context = self.get_context_data(object=self.object)

#         return self.render_to_response(context)

def FilialDetalhesView(request, slug, *args, **kwargs):
    object_list = get_object_or_404(Filias, slug=slug)
    object_list.filiais_views=object_list.filiais_views+1
    object_list.save()

    comentarios = object_list.comentarios.filter(active=True, resposta__isnull=True)
    if request.method == 'POST':
        comment_form = ComentarioForm(data=request.POST)
        if comment_form.is_valid():
            resposta_obj = None
        try:
            resposta_id = int(request.POST.get('resposta_id'))
        except:
            resposta_id = None
        if resposta_id:
            resposta_obj = Comentario.objects.get(id=resposta_id)
            if resposta_obj:
                reply_comment = comment_form.save(commit=False)
                reply_comment.resposta = resposta_obj
        new_comment = comment_form.save(commit=False)
        new_comment.comentario = object_list
        new_comment.save()
        return redirect('filiais:filiais_detalhes', slug)
    else:
        comment_form = ComentarioForm()

    return render(request, 'filiais_detalhes.html', {'object_lists':object_list, 'comment_form':comentarios, 'comment_form':comment_form})