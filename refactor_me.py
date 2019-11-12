#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter

Expense = namedtuple('Expense', ('category', 'amount'))


def sum_expenses(expenses, min_amount=0):
    aggregated_expenses = defaultdict(int)
    for expense in expenses:
        amount = expense.amount
        if amount >= min_amount:
            aggregated_expenses[expense.category] += amount
    return aggregated_expenses


def print_expenses(expenses):
    sorted_expenses = sorted(expenses.items(), key=itemgetter(1))
    for category, amount in sorted_expenses:
        print(category, amount)


if __name__ == '__main__':
    # TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3), Expense('dog', 1))
    aggregated_expenses = sum_expenses(test_expenses, 2)
    print_expenses(aggregated_expenses)
