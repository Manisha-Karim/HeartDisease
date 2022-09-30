from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home),
    path('predict/',views.predict),
    path('predict/result', views.results),
    path('predict/result/predictions.html', views.prediction),


]
