from rest_framework import serializers
from .models import Autor, Ksiazka, Czytelnik, Kategoria, Wypozyczenie, STATUS_KSIAZKI, JEZYKI
from datetime import date


# Serializator dla modelu Ksiazka
class KsiazkaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Pole tylko do odczytu, generowane automatycznie
    tytul = serializers.CharField(required=True)  # Pole wymagane, musi być podany tytuł
    jezyk = serializers.ChoiceField(choices=JEZYKI.choices, default=JEZYKI.Angielski)  # Wybór języka
    status = serializers.ChoiceField(choices=STATUS_KSIAZKI, default=STATUS_KSIAZKI[0][0])  # Wybór statusu książki
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())  # Klucz obcy do autora
    kategoria = serializers.PrimaryKeyRelatedField(queryset=Kategoria.objects.all(), allow_null=True)  # Klucz obcy do kategorii (opcjonalny)
    rok_publikacji = serializers.IntegerField(required=False)  # Rok publikacji (opcjonalny)

    def validate_tytul(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Tytuł musi mieć przynajmniej 3 znaki!")
        return value

    def create(self, validated_data):
        return Ksiazka.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.jezyk = validated_data.get('jezyk', instance.jezyk)
        instance.status = validated_data.get('status', instance.status)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.kategoria = validated_data.get('kategoria', instance.kategoria)
        instance.rok_publikacji = validated_data.get('rok_publikacji', instance.rok_publikacji)
        instance.save()
        return instance


# Serializator dla modelu Autor
class AutorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Imię może zawierać tylko litery!")
        return value

    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nazwisko może zawierać tylko litery!")
        return value

    def create(self, validated_data):
        return Autor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.save()
        return instance


# Serializator dla modelu Czytelnik
class CzytelnikSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uzytkownik = serializers.PrimaryKeyRelatedField(queryset=Czytelnik.objects.all())  # Klucz obcy do użytkownika
    wypozyczone_ksiazki = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all(), many=True)

    def create(self, validated_data):
        return Czytelnik.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.uzytkownik = validated_data.get('uzytkownik', instance.uzytkownik)
        instance.wypozyczone_ksiazki.set(validated_data.get('wypozyczone_ksiazki', instance.wypozyczone_ksiazki.all()))
        instance.save()
        return instance


# Serializator dla modelu Kategoria
class KategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(required=False)

    def create(self, validated_data):
        return Kategoria.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance


# Serializator dla modelu Wypozyczenie
class WypozyczenieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    czytelnik = serializers.PrimaryKeyRelatedField(queryset=Czytelnik.objects.all())  # Klucz obcy do czytelnika
    ksiazka = serializers.PrimaryKeyRelatedField(queryset=Ksiazka.objects.all())  # Klucz obcy do książki
    data_wypozyczenia = serializers.DateField(default=date.today)
    data_zwrotu = serializers.DateField(required=False)

    def create(self, validated_data):
        return Wypozyczenie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.czytelnik = validated_data.get('czytelnik', instance.czytelnik)
        instance.ksiazka = validated_data.get('ksiazka', instance.ksiazka)
        instance.data_wypozyczenia = validated_data.get('data_wypozyczenia', instance.data_wypozyczenia)
        instance.data_zwrotu = validated_data.get('data_zwrotu', instance.data_zwrotu)
        instance.save()
        return instance