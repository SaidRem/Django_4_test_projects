from django.urls import path
from .views import current_time, workdir, index

urlpatterns = [
    path('', index, name='index'),
    path('curtime/', current_time, name='current time'),
    path('workdir/', workdir, name='work directory')
]