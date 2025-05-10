from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class BudgetData(models.Model):
    NOURRITURE = "Nourriture"
    HYGIENE = "Hygiène"
    FACTURES = "Factures"
    ALCOOL = "Alcool"
    JEUX = "Jeux"

    CATEGORY_CHOICES = [
        (NOURRITURE, "Nourriture"),
        (HYGIENE, "Hygiène"),
        (FACTURES, "Factures"),
        (ALCOOL, "Alcool"),
        (JEUX, "Jeux"),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=NOURRITURE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_added = models.DateTimeField(default=timezone.now)
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.category} ID: {self.id}"


class IncomeData(models.Model):
    user_income = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Vous pouvez ajouter un champ category s'il est nécessaire dans votre modèle


    def __str__(self):
        return f"Income: {self.income} DH for {self.user_income}"