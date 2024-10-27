def print_params(a = 1, b = 'Str', c = True):
    print(a, b ,c)

print_params(2, 'Привет', True)
print_params(23, 'Алтай', False)

print_params(4, 25, [1,2,3])
print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров

vales_list = [15, 'Алтай' True]
vales_dict = {'a': 15, 'b': 'ветер', 'c': True}
print(*vales_list, **vales_dict)

# Распаковка + отдельные параметры
vales_list_2 = [54.32, 'Алтай']
print_params(*vales_list_2, 42)
print(vales_list_2)