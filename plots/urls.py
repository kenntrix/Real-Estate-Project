from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plots'),
    # path('<int:pk>/', views.details, name='plot_detail' ),
    # path('add/', views.create, name='plot_create'),
    # path('<int:pk>/edit/', views.edit, name='plot_edit'),
    # path('<int:pk>/delete/', views.delete, name='plot_delete'),
]