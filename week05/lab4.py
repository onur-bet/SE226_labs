x= int(input("Enter number of users:"))

Dict={}

for i in range(x):
    name=input("Enter name:")

    Dict.setdefault(name,[])

    itemcount=int(input("How many items?"))
    for j in range(itemcount):
        item=input(f"Item  {j+1}:")
        Dict[name].append(item)


print("USER DATA:")
for key in Dict:
    print(key ,"->" ,Dict[key])
    print("\n")


user_sets = {user: set(items) for user, items in Dict.items()}

unique_items = {}

for user in user_sets:
    others = set()

    for other_user in user_sets:
        if other_user != user:
            others = others | user_sets[other_user]

    unique_items[user] = user_sets[user] - others

print("UNIQUE ITEMS:")
print(unique_items)

common = user_sets[list(user_sets.keys())[0]]

for user in user_sets:
    common = common & user_sets[user]

print("COMMON ITEMS:")
print(common)

