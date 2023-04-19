#!/bin/python3
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]



# Calculate average price of haircuts

total_price = 0

for price in prices:

  total_price += price



average_price = total_price / len(prices)

print("Average Haircut Price: {}".format(average_price))



# Reduce all prices by 5 dollars

new_prices = [price - 5 for price in prices]

print(new_prices)



# Calculate total revenue

total_revenue = 0

for i in range(len(hairstyles)):

  total_revenue += prices[i] * last_week[i]



print("Total Revenue: {}".format(total_revenue))



# Calculate average daily revenue

average_daily_revenue = total_revenue / 7

print("Average Daily Revenue: {}".format(average_daily_revenue))



# Create a list of haircuts that cost less than 30 dollars

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)


