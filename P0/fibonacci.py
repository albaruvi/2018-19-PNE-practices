number = int(input('Please introduce a number'))


def fibonacci(num):
    f = 0
    n = 1
    list_numbers = []
    for i in range(num):
        list_numbers.append(f)
        f, n = n, f+n
    return list_numbers


total_series = fibonacci(number)
print('The total fibonacci series is', total_series)
