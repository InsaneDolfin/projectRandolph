from django.urls import path

from . import views


app_name = 'randolphApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('jeux', views.jeux, name='jeux'),
    path('jeux/<int:name_id>/', views.detail, name='detail'),

]
