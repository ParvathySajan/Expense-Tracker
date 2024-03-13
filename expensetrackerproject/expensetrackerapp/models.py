from django.db import models

# Create your models here.
class Expense(models.Model):
    expense_name=models.CharField(max_length=100)
    amount=models.BigIntegerField()

    def __str__(self):
        return self.expense_name

class Balance(models.Model):
    balance_amount=models.BigIntegerField()

    def __str__(self):
        return self.balance_amount

