# # example 1
# viewer = "🐊"
# owner = "🐼"
# editor = "🐓"

# print(viewer)
# print(owner)
# print(editor)

# ## better 1
# print(f"{viewer=}")
# print(f"{owner=}")
# print(f"{editor=}")

# viewer = "📺"
# owner = "💻"
# editor = "⌨️"

# print(f"{viewer=}")
# print(f"{owner=}")
# print(f"{editor=}")



# # example 2
# float_variable = 3.141592653589793

# print(f"{float_variable:.2f}")

# h1 = "Искусство IT"
# text = "текст выше мы и центрируем"
# # print(f"{h1:^25}\n{text}")
# print(f"{f'** {h1} **':^25}\n{text}")

# def myfunc(x, y, z):
#     print(x, y, z)

# tuple_vec = (1, 0, 1)
# dict_vec = {'x': 1, 'y': 0, 'z': 1}

# myfunc(*tuple_vec)
# # 1, 0, 1

# myfunc(**dict_vec)
# # 1, 0, 1

# number = 254.3463
# print(f"{f'${number:.3f}':>10s}")
# '  $254.346'

# output
#  '  hello world  '


# number = 1234567890
# print(f"{number:,}")

# 1,234,567,890


# # example 3
# money = 3_142_671.76 # 💡 Это тоже самое, что и 3142671.76

# print(f"${money:,.2f}")



# # example 4
# owl = '🦉'

# print(f'{owl!a}')