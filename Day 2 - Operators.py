#!/bin/python3

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent/100) * meal_cost
    tax = (tax_percent/100) * meal_cost
    total_cost = meal_cost + tip + tax
    total_cost = round(total_cost)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
