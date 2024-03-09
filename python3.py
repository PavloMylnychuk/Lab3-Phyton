from collections import defaultdict

database = defaultdict(lambda: defaultdict(int))

while True:
    try:
        input_line = input().split()
        if not input_line:
            break

        buyer, item, quantity = input_line
        database[buyer][item] += int(quantity)

    except ValueError:
        break

buyers = sorted(database.keys())
for buyer in buyers:
    print(f"{buyer}:")
    for item, quantity in sorted(database[buyer].items()):
        print(f"{item} {quantity}")
