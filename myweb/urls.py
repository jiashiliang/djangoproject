import views
from django.urls import path, include

from myweb.views import home,test,tiao

urlpatterns = [
    path('home/',home),
    path('test/',test),
    path('tiao/',tiao)

]
