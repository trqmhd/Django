from django.conf.urls import url
from basic_app import views
from django.urls import path, include


app_name = 'basic_app'

urlpatterns = [


    url(r'^register/$', views.register, name = 'register'),
    #path('basic_app/', include('basic_app.url'))
    url(r'^user_login/$', views.user_login,name='user_login')


]

