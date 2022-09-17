from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('consoles/', views.consoles_index, name='index'),
    path('consoles/<int:console_id>/', views.console_detail, name="detail"),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='console_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name="console_update"),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name="console_delete"),
]