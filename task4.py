import numpy as np

usage = np.array([
    [12, 14, 11, 13, 15, 18, 16],
    [22, 25, 21, 24, 23, 30, 28],
    [8, 9, 7, 10, 9, 12, 11],
    [18, 17, 19, 16, 20, 26, 24],
    [14, 13, 15, 12, 16, 21, 19]
])

house_numbers = np.arange(1, 6)

days = np.array([
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
])

print("\n========== PART A: BASICS ==========\n")

print("Shape:", usage.shape)
print("Size:", usage.size)
print("Ndim:", usage.ndim)
print("Data Type:", usage.dtype)

print("\nHouse 3 Weekly Data:")
print(usage[2])

print("\nFriday Data of All Houses:")
print(usage[:, 4])

print("\nWeekend Data (Saturday and Sunday):")
print(usage[:, 5:7])

print("\n========== PART B: ANALYSIS ==========\n")

weekly_total = np.sum(usage, axis=1)

print("Weekly Consumption of Each House:")
print(weekly_total)

daily_average = np.mean(usage, axis=0)

print("\nDaily Average Consumption:")
print(daily_average)

maximum_usage = np.max(weekly_total)
minimum_usage = np.min(weekly_total)

maximum_house = np.argmax(weekly_total) + 1
minimum_house = np.argmin(weekly_total) + 1

print("\nHighest Consumption:")
print("House Number:", maximum_house)
print("Units:", maximum_usage)

print("\nLowest Consumption:")
print("House Number:", minimum_house)
print("Units:", minimum_usage)

daily_total = np.sum(usage, axis=0)

highest_day_index = np.argmax(daily_total)

print("\nDaily Total Consumption:")
print(daily_total)

print("Highest Consumption Day:", days[highest_day_index])
print("Total Units:", daily_total[highest_day_index])

weekday_average = np.mean(usage[:, 0:5])
weekend_average = np.mean(usage[:, 5:7])

print("\nWeekday Average Consumption:", weekday_average)
print("Weekend Average Consumption:", weekend_average)

if weekend_average > weekday_average:
    print("Weekend consumption is higher.")
else:
    print("Weekday consumption is higher.")

print("\n========== PART C: FILTERING ==========\n")

greater_than_20 = usage[usage > 20]

print("Readings Greater Than 20:")
print(greater_than_20)

count = np.count_nonzero(usage > 20)

print("Total Readings Greater Than 20:", count)

average_weekly = np.mean(weekly_total)

above_average_houses = np.where(
    weekly_total > average_weekly
)[0] + 1

print("\nAverage Weekly Consumption:", average_weekly)
print("Houses Above Average Consumption:", above_average_houses)

bills = np.where(
    weekly_total <= 100,
    weekly_total * 25,
    weekly_total * 35
)

print("\nElectricity Bills:")
print("House Numbers:", house_numbers)
print("Weekly Units:", weekly_total)
print("Bills (Rs.):", bills)

usage_labels = np.where(
    weekly_total > 100,
    "High Usage",
    "Normal Usage"
)

print("\nUsage Categories:")
print(usage_labels)

print("\n========== PART D: CHALLENGE ==========\n")

ranking = np.argsort(weekly_total)[::-1]

ranked_houses = house_numbers[ranking]
ranked_consumption = weekly_total[ranking]

print("Houses Ranking (Highest to Lowest):")
print(ranked_houses)

print("Weekly Consumption:")
print(ranked_consumption)

minimum_value = np.min(usage)
maximum_value = np.max(usage)

normalized_data = (
    (usage - minimum_value) /
    (maximum_value - minimum_value)
)

normalized_data = np.round(normalized_data, 2)

print("\nNormalized Data:")
print(normalized_data)

new_usage = usage.astype(float)

new_usage[2] = new_usage[2] * 1.20

new_weekly_total = np.sum(new_usage[2])

print("\nOriginal House 3 Data:")
print(usage[2])

print("\nNew House 3 Data:")
print(new_usage[2])

print("\nOriginal Weekly Consumption:", weekly_total[2])
print("New Weekly Consumption:", new_weekly_total)