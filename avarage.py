
def divisor(a):
    list_divisor = []
    for i in range(1, a+1):
        if a % i == 0:
            list_divisor.append(i)
    return list_divisor


def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return 'not prime'
                break
        else:
            return 'prime'

    else:
        return 'not prime'


list_numbers = []
for i in range(10):
    number = int(input())
    list_numbers.append(number)
list_numbers = map(int, list_numbers)
list_numbers = list(list_numbers)
list_empty = []
dict_numbers = dict()
while list_numbers != list_empty:
    number = list_numbers.pop()
    dict_numbers[number] = divisor(number)


for i in dict_numbers:
    num = dict_numbers.get(i)
    num = list(map(prime, num))
    num = num.count('prime')
    dict_numbers[i] = num

number_prime = dict_numbers.values()
max_prime = max(number_prime)

list_prime_max = []
for i in dict_numbers:
    if dict_numbers[i] == max_prime:
        list_prime_max.append(i)

result = max(list_prime_max)
print(result, max_prime)
