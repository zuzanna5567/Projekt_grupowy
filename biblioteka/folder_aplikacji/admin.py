from django.contrib import admin
from .models import Kategoria, Autor, Ksiazka, Czytelnik, Wypozyczenie

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']
admin.site.register(Kategoria, KategoriaAdmin)

class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ["tytul", "autor", "kategoria", "rok_publikacji", "jezyk", "status"]
    list_filter = ["autor"]
admin.site.register(Ksiazka, KsiazkaAdmin)

class AutorAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko"]
    list_filter = ['nazwisko']
admin.site.register(Autor, AutorAdmin)

class CzytelnikAdmin(admin.ModelAdmin):
    list_display = ["uzytkownik", "get_wypozyczone_ksiazki"]
    list_filter = ['uzytkownik']

    def get_wypozyczone_ksiazki(self, obj):
        return ", ".join([ksiazka.tytul for ksiazka in obj.wypozyczone_ksiazki.all()])
    get_wypozyczone_ksiazki.short_description = 'Wypożyczone Książki'
admin.site.register(Czytelnik, CzytelnikAdmin)

class WypozyczenieAdmin(admin.ModelAdmin):
    @admin.display(description="Czytelnik (ID)")
    def czytelnik_with_id(self, obj):
        if obj.czytelnik:
            return f'{obj.czytelnik.nazwa} ({obj.czytelnik.id})'
        return "Brak czytelnika"

    list_display = ['czytelnik_with_id', 'ksiazka', 'data_wypozyczenia', 'data_zwrotu']
    list_filter = ["czytelnik_with_id"]
admin.site.register(Wypozyczenie)