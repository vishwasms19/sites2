from django.conf.urls import url
from authapp import views

urlpatterns = [
    url(r'^registration$',views.userregistration),
    url(r'^login$', views.userlogin),
    url(r'^logout$', views.userlogout),
    url(r'^dashboard$', views.dashboard)
]

