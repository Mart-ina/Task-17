numbers = list(map(int,(input("Введите целые числа через пробел:\n").split())))
num = int(input("Введите число:\n"))
numbers.append(num)

def sort_ed(numbers):
    for i in range(len(numbers)):
        x = numbers[i]
        idx = i
        while idx > 0 and numbers[idx - 1] > x:
            numbers[idx] = numbers[idx - 1]
            idx -= 1
        numbers[idx] = x
    return numbers
print("Список по возрастанию: ",sort_ed(numbers))


def binary_search(numbers, num, left, right):
    if left > right:
        return False

    middle = (right+left) // 2
    if numbers[middle] == num:
        return middle
    elif num < numbers[middle]:

        return binary_search(numbers, num, left, middle-1)
    else:
        return binary_search(numbers, num, middle+1, right)

print("Индекс числа, которое меньше введенного пользователем:", (binary_search(numbers, num, 0, (len(numbers)-1)))-1)



