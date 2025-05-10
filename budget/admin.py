from django.contrib import admin

from .models import BudgetData, IncomeData

admin.site.register(BudgetData)
admin.site.register(IncomeData)