n = 15
prices = [50, 30, 40, 25, 35]
circulation = [12000, 8000, 15000, 5000, 9000]

total_cost = 0
total_circulation = 0

for i in range(n):
    if circulation[i] < 10000:
        total_cost += prices[i] * circulation[i]
        total_circulation += circulation[i]

average_cost = total_cost / total_circulation if total_circulation > 0 else 0

print(f"Average cost of magazines with circulation less than 10000: {average_cost}")
