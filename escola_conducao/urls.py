from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('alunos/', include('alunos.urls')),
    path('instrutores/', include('instrutores.urls')),
    path('aulas/', include('aulas.urls')),
    path('exames/', include('exames.urls')),
    path('pagamentos/', include('pagamentos.urls')),
    path('financeiro/', include('financeiro.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)