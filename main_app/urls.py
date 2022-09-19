from django.urls import path
from . import views

urlpatterns = [
    # General Routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Console Routes
    path('consoles/', views.consoles_index, name='index'),
    path('consoles/<int:console_id>/', views.console_detail, name="detail"),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='console_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name="console_update"),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name="console_delete"),
    # Accessory Routes
    path('consoles/<int:console_id>/add_accessory', views.add_accessory, name='add_accessory'),
    # Games Routes
    path('games/', views.GameList.as_view(), name='games_index'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game_detail'),
    path('games/create/', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='game_delete'),
    path('consoles/<int:console_id>/assoc_game/<int:game_id>/', views.assoc_game, name="assoc_game"),
    path('consoles/<int:console_id>/unassoc_game/<int:game_id>/', views.unassoc_game, name="unassoc_game"),
    # Signup Route
    path('accounts/signup/', views.signup, name='signup'),
]