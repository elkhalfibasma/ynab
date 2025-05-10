from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal

from .forms import AddIncome, AddItem
from .models import BudgetData, IncomeData

@login_required
def budget(request):
    expense_items = BudgetData.objects.filter(user_expense=request.user).order_by(
        "-date_added"
    )

    # Setting up pagination per expense_items
    paginator = Paginator(expense_items, 10, 3)  # Show 10 items per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Calculer le total des dépenses de l'utilisateur actuel
    total_cost_dict = BudgetData.objects.filter(user_expense=request.user).aggregate(
        total_cost=Sum("cost")
    )
    total_cost = total_cost_dict['total_cost'] if total_cost_dict['total_cost'] is not None else Decimal(0)

    # Calculer le total des revenus de l'utilisateur actuel
    total_income_dict = IncomeData.objects.filter(user_income=request.user).aggregate(
        total_income=Sum("income")
    )
    total_income = total_income_dict['total_income'] if total_income_dict['total_income'] is not None else Decimal(0)

    # Calculer le montant restant
    amount_left = total_income - total_cost

    # Instantiating the forms
    a_form = AddItem()
    b_form = AddIncome()

    
    if request.method == "POST":
        if "add-item" in request.POST:
            a_form = AddItem(request.POST)
            if a_form.is_valid():
                a_form = a_form.save(commit=False)
                a_form.user_expense = request.user
                a_form.date_added = timezone.now()
                a_form.save()
                return HttpResponseRedirect(reverse("budget"))
        elif "add-income" in request.POST:
            b_form = AddIncome(request.POST)
            if b_form.is_valid():
                b_form = b_form.save(commit=False)
                b_form.user_income = request.user
                b_form.date_added = timezone.now()
                b_form.save()
                return HttpResponseRedirect(reverse("budget"))

    return render( request,"budget/budget.html",
        context={
            "user": request.user,
            "expense_items": expense_items,
            "total_cost": total_cost,
            "total_income": total_income,
            "a_form": a_form,
            "b_form": b_form,
            "page_obj": page_obj,
            "amount_left": amount_left,
        },
    )

def delete_item(request, user_id):
    item = BudgetData.objects.get(id=user_id)
    item.delete()
    messages.success(request, ("Item Deleted!"))
    return redirect("budget")

@login_required
def ajout(request):
    if request.method == 'POST':
        form = AddItem(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user_expense = request.user  # Assigne l'utilisateur actuel à l'objet
            new_item.save()
            return redirect('budget')  # Redirection vers la page du budget après l'ajout réussi
    else:
        form = AddItem()
    return render(request, 'ajout.html', {'form': form})

from .forms import AddIncome
from .models import IncomeData

def add_income(request):
    if request.method == 'POST':
        form = AddIncome(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user_income = request.user
            income.save()
            messages.success(request, 'Income added successfully.')
            return render(request, 'budget/ajout.html', {'income': income})
        else:
            messages.error(request, 'Failed to add income. Please check the form data.')
    else:
        form = AddIncome()
    return render(request, 'budget/budget.html', {'form': form})
