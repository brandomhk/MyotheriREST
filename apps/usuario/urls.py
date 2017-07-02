from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'^usuario/$', UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
