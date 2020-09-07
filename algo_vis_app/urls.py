from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='algo-vis-app-home'),
    path('bubble-sort/', views.Bubble_Sort, name='bubble-sort-view')
    #path('about/', views.about, name='algo-vis-app-about'),

]