from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=100, default="Brak nazwy")  # Domyślna nazwa
    weight = models.FloatField(default=0.0)  # Domyślna waga
    sets = models.IntegerField(default=0)  # Domyślna liczba serii
    reps = models.IntegerField(default=0)  # Domyślna liczba powtórzeń
    updated = models.DateTimeField(auto_now=True)  # Data ostatniej aktualizacji
    created = models.DateTimeField(auto_now_add=True)  # Data utworzenia

    def __str__(self):
        return self.name  # Wyświetlanie nazwy ćwiczenia w adminie
