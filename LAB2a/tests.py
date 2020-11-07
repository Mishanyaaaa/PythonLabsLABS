print("1 константа", True)
print("2 константа", False)
print("3 константа", None)
a = 1232
a = str(a)
print(f'a, type(a) = {type(a)}')
#Цикли та розгалуження
def range_of_nums(XXL):

    if XXL:
        j = 0
    else:
        j = 1
    for i in range(j,101,2):
        print(i)
range_of_nums(True)

A = 0
A1 = 'fff'
try:
    print("Що буде якщо A>A1", A>A1, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")
path = "README.md"
name = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", name)
with open(path, 'a') as f_obj:
    f_obj.write(f'і таке буває. {name("Mishanyaa", "Kaminskyi")}')

