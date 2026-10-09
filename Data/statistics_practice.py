def count_above_average(numbers,v):
    if numbers==[]:
        return 0
    s=0
    for number in numbers:
        if number>v:
            s+=1
    return s
def average(numbers):
    if len(numbers) == 0:
        return None

    s = 0
    for number in numbers:
        s += number

    print(s / len(numbers))
    return s / len(numbers)
print(count_above_average([1, 2, 9],average([1, 2, 9])))