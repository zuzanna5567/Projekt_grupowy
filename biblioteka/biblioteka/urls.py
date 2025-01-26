from django.contrib import admin
from django.urls import path
from folder_aplikacji import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('kategorie/', views.kategoria_list, name='kategoria_list'),
    path('kategorie/<int:pk>/', views.kategoria_details, name='kategoria_detail'),
    path('kategorie/<int:pk>/delete/', views.kategoria_details, name='kategoria_delete'),
    path('kategorie/<int:pk>/update/', views.kategoria_details, name='kategoria_update'),

    path('autorzy/', views.autor_list, name='autor_list'),
    path('autorzy/<int:pk>/', views.autor_details, name='autor_detail'),
    path('autorzy/<int:pk>/delete/', views.autor_details, name='autor_delete'),
    path('autorzy/<int:pk>/update/', views.autor_details, name='autor_update'),

    path('ksiazki/', views.ksiazka_list, name='ksiazka_list'),
    path('ksiazki/<int:pk>/', views.ksiazka_details, name='ksiazka_detail'),
    path('ksiazki/<int:pk>/delete/', views.ksiazka_details, name='ksiazka_delete'),
    path('ksiazki/<int:pk>/update/', views.ksiazka_details, name='ksiazka_update'),

    path('czytelnicy/', views.czytelnik_list, name='czytelnik_list'),
    path('czytelnicy/<int:pk>/', views.czytelnik_details, name='czytelnik_detail'),
    path('czytelnicy/<int:pk>/delete/', views.czytelnik_details, name='czytelnik_delete'),
    path('czytelnicy/<int:pk>/update/', views.czytelnik_details, name='czytelnik_update'),

    path('wypozyczenia/', views.wypozyczenie_list, name='wypozyczenie_list'),
    path('wypozyczenia/<int:pk>/', views.wypozyczenie_details, name='wypozyczenie_detail'),
    path('wypozyczenia/<int:pk>/delete/', views.wypozyczenie_details, name='wypozyczenie_delete'),
    path('wypozyczenia/<int:pk>/update/', views.wypozyczenie_details, name='wypozyczenie_update'),

    path('welcome/', views.welcome_view, name='welcome_view'),
]
