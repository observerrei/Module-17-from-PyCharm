def inp_ut():
    int_nums = input("Введите числа через пробел: ")
    orig_list = list(map(int, int_nums.split(" ")))
    return orig_list

orig_list_num = inp_ut()
num1 = int(input("Введите любое число: "))

nums_list = orig_list_num.copy()  #на всякий случай копируем неотсортированный список

for i in range(len(orig_list_num)):
    for j in range(len(orig_list_num) - i - 1):
        if orig_list_num[j] > orig_list_num[j + 1]:
            orig_list_num[j], orig_list_num[j + 1] = orig_list_num[j + 1], orig_list_num[j]


def binary_search(orig_list_num: list, num1):
    left, right = 0, len(orig_list_num)
    if num1 == orig_list_num[-1]:
        print('Число не соответствует всем заданным условиям: в последовательности нет числа, больше введенного!')

    while left < right:
        middle = (left + right) // 2
        if orig_list_num[middle] < num1:
            left = middle + 1
        else:
            right = middle
    return left - 1

print('Сортировка списка по возрастанию элементов: ', orig_list_num)
print("Номер позиции элемента, меньшей позиции введенного пользователем числа: ", binary_search(orig_list_num, num1))