# test time: 22 января 2018 г. 14:19:24 (MSK)

# traditional list with test mass values
l = []
mass = (4, 30, 50, 90, 45, 33, 12, 144)
for x in mass:
    if x % 3 == 0 and x % 4 == 0:
        l.append(x ** 3)
print(l)

# list comprehension
new_list = [(i ** 3) for i in mass if i % 3 == 0 and i % 4 == 0]
print(new_list)
