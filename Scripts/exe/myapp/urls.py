from django.urls import path
from . import views
 
urlpatterns = [

    path('', views.welcome),
    path('person/show/', views.person_show, name='person_show'),
    path('person/<int:pk>/delete/', views.delete_person, name='delete_person'),
    path('people/', views.person_list, name='person_list'),
    path('person/create/', views.person_create, name='person_create'),
    path('person/update/<int:pk>/', views.person_update, name='person_update'),  
]