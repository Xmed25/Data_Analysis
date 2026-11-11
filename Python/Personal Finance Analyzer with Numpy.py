import numpy as np

days = np.array([
    "Saturday", "Sunday", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday"
])

expenses = np.array([
    [120, 50, 200, 0, 100],
    [80, 30, 0, 50, 40],
    [150, 20, 100, 0, 60],
    [90, 40, 300, 0, 0],
    [200, 50, 0, 80, 30],
    [100, 30, 150, 0, 70],
    [50, 20, 0, 100, 40]
])

categories = np.array([
    "Food", "Transport", "Shopping",
    "Bills", "Entertainment"
])


daily_totals = expenses.sum(axis=1)

for d in range(len(days)):

    print(f"\n{days[d]}")

    for c in range(len(categories)):
        print(f"{categories[c]}: {expenses[d][c]} EGP")

    print(f"Total Daily Spending: {daily_totals[d]} EGP")
    print(f"Daily Average: {expenses[d].mean():.2f} EGP")

    max_index = np.argmax(expenses[d])
    print(f"Largest Category: {categories[max_index]}")


high_index = np.argmax(daily_totals)
low_index = np.argmin(daily_totals)

print("\n========== SUMMARY ==========")

print(f"Highest Spending Day: {days[high_index]}")
print(f"Lowest Spending Day: {days[low_index]}")


category_totals = expenses.sum(axis=0)

for c in range(len(categories)):
    print(f"{categories[c]}: {category_totals[c]} EGP")

largest_category = np.argmax(category_totals)

print(f"\nLargest Expense Category: {categories[largest_category]}")


print(f"\nTotal Weekly Spending: {expenses.sum()} EGP")
print(f"Average Daily Spending: {daily_totals.mean():.2f} EGP")
