from django.urls import path, include

from . import views
urlpatterns = [
    
    path('', views.index ,name='index'),
    path('book/', views.book ,name='book'),
    path('update/', views.update ,name='update'),
    path('delete/', views.delete ,name='delete'),
]
