from django.urls import path, include
from . import views

app_name = "wines"
urlpatterns = [
    path("",views.index,name="index"),
    path("results/<str:query>",views.results, name = "results")
]