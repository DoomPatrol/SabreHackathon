from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from travel_app import views

urlpatterns = [
    url(r'^$', views.the_dashboard, name='dashboard'),
]
