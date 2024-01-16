from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include(('{{ project_name }}.core.urls', 'core'), namespace='core')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path(r'__debug__/', include(debug_toolbar.urls)))