import numpy as np

temperatures = np.array([
    [25, 27, 26, 29, 31, 30, 28],  # Cairo
    [20, 22, 21, 23, 25, 24, 22],  # London
    [15, 17, 16, 18, 1, 19, 17]   # Moscow
])

cities = ["Cairo", "London", "Moscow"]

days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]


for city,temp in zip(cities ,temperatures):
  print(f"{city} -> average:{temp.mean() : .2f}")

print(f"\nMaximum temperature: {temperatures.max()}")
print(f"Minimum temperature: {temperatures.min()}\n")

for city,temp in zip(cities,temperatures):
  print(f"City: {city}   Coldest Day: {days[temp.argmin()]}")
  print(f"City: {city}   Hottest Day: {days[temp.argmax()]}")

for city, temp in zip(cities, temperatures):

    changes = np.diff(temp)

    print(f"\n{city}")
    print(f"Daily Changes: {changes}")
