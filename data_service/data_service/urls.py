from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from json_reader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^stateToCode/$',views.stateToCode),
    url(r'^codeToState/$',views.codeToState)
]
