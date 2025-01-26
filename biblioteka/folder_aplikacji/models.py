from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Statyczne listy wyboru
JEZYKI = models.TextChoices('Języki', 'Polski Angielski Niemiecki Francuski Hiszpański')

STATUS_KSIAZKI = (
    ('D', 'Dostępna'),
    ('Z', 'Zarezerwowana'),
    ('W', 'Wypożyczona'),
)

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50, unique=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

class Autor(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=120)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.SET_NULL)
    rok_publikacji = models.PositiveIntegerField(null=True, blank=True)
    jezyk = models.CharField(max_length=20, choices=JEZYKI.choices, default=JEZYKI.Angielski)
    status = models.CharField(max_length=1, choices=STATUS_KSIAZKI, default=STATUS_KSIAZKI[0][0])

    def __str__(self):
        return f"{self.tytul} by {self.autor}"
    
    class Meta:
        ordering = ['tytul']  # Posortowane alfabetycznie po tytule.

class Czytelnik(models.Model):
    uzytkownik = models.OneToOneField(User, on_delete=models.CASCADE)
    wypozyczone_ksiazki = models.ManyToManyField(Ksiazka, blank=True, through='Wypozyczenie')

    def __str__(self):
        return self.uzytkownik.username
    
    class Meta:
        ordering = ['uzytkownik__username']  # Posortowanie alfabetycznie według username.

class Wypozyczenie(models.Model):
    czytelnik = models.ForeignKey(Czytelnik, on_delete=models.CASCADE)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    data_wypozyczenia = models.DateField(default=date.today)
    data_zwrotu = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.czytelnik} wypożyczył(a) {self.ksiazka.tytul} dnia {self.data_wypozyczenia}"
    
    class Meta:
        ordering = ['data_wypozyczenia']  # Posortowane od najstarszego do najnowszego.