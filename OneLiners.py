

# example 1
sizes = input()
sizes = sizes.strip()
sizes = sizes.split()
x = sizes[0]
y = sizes[1]
z = sizes [2]

## better 1
x, y, z = input().strip().split()


# example 2
x = int(x)
y = int(y)
z = int(z)

## better 2.1
x, y, z = map(int, (x, y, z))

## maybe better 2.2
from functools import reduce

volume = reduce(
    lambda x, y: x * y,
    map(int, input().strip().split())
)


# example 3
names = ["Христофор", "Адемар", "Том", "Стефан", "Авраам"]
names_starts_a = []
for name in names:
    if name.startswith("А"):
        names_starts_a.append(name)

## better 3
names = ["Христофор", "Адемар", "Том", "Стефан", "Авраам"]
names_starts_a = [name for name in names if name.startswith("А")]


# example 4
if name == "Alex" or name == "Petr" or name == "Christ":
    print(name)

## better 4
if name in ("Alex", "Petr", "Christ"):
    print(name)


# example 5
a = b = c = d = e = True
if a and b and c and d and e:
    print("All true")

## better 5
if all((a, b, c, d, e)): # all true?
    print("All true")

if any((a, b, c, d, e)): # at least one true
    print("one more true")


# better example 6 ternary operator
admin_email = "admin@gmail.com" if config.IS_PRODUCTION else "another@gmail.com"
