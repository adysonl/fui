from django.urls import path
from signup import views
urlpatterns = [
    path('', views.cadastro_usuario, name = 'signup')
]
