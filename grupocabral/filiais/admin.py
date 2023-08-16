from django.contrib import admin
from .forms import  FilialForm
from .models import Filias, Comentario, Foto

class FotoInline(admin.TabularInline):
    model = Foto
    max_num = 0
    readonly_fields = ('fotos',)

class FiliasAdmin(admin.ModelAdmin):
	form = FilialForm
	inlines = [
        FotoInline, 
        ]
	list_display = ('filial','fotos')
	prepopulated_fields = {"slug": ("filial",)}

	@admin.display(description='CRIADO EM')
	def admin_data(self, obj):
		return obj.data.strftime('%d/%m/%Y')

	def save_related(self, request, form, formsets, change):
		super().save_related(request, form, formsets, change)
		form.save_photos(form.instance)

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'email', 'data_criada', 'active']

admin.site.register(Filias, FiliasAdmin)
admin.site.register(Comentario, ComentarioAdmin)