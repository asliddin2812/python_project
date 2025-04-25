from django.urls import path
from .views import history,frameworks,libraries,documentation,home

urlpatterns = [

    path('history/', history, name='history'),
    path('frameworks/', frameworks, name='frameworks'),
    path('libraries/', libraries, name='libraries'),
    path('documentation/', documentation, name='documentation'),
    path('home/', home, name='home'),
    path('', home, name='index'),
]
