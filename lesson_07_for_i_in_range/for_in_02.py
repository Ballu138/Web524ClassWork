# start = int(input("Введите начало вашей последовательности."))
# end = int(input("Введите до какого значения будет идти последовательность (включительно/не включая)."))

start = 2
end = 5
# тонкая грань в условии на ввод.

for i in range(start, end):  # не включая
    print(f'Значение в цикле: i = {i}')
print(f'Значение вне цикла: i = {i}')
print()

for i in range(start, end + 1):  # включительно
    print(f'Значение в цикле: i = {i}')
print(f'Значение вне цикла: i = {i}')
print()

for i in range(start + 1, end):  # между
    print(f'Значение в цикле: i = {i}')
print(f'Значение вне цикла: i = {i}')
print()

for i in range(-10, 0):
    print(i)
