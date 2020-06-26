from django.conf.urls import url
from django.conf.urls import include
from fourApp import views

# TEMPLATE TAGGING
app_name = 'fourApp'

urlpatterns=[
    url(r'^relative/',views.relative,name='relative'),
    url(r'^other/', views.other,name='other'),
    url(r'^base/', views.base,name='base'),

]
