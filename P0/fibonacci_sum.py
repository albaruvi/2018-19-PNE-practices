number = int(input('Please introduce a number'))


def fibonacci(num):
    f = 0
    n = 1
    list_numbers = []
    for i in range(num):
        list_numbers.append(f)
        f, n = n, f+n
    sum1 = 0
    for a in list_numbers:
        sum1 = sum1 + a
    return sum1


total_series = fibonacci(number)
print('The total fibonacci series sum is', total_series)
