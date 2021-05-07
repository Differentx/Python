# Diff

def sum_of_two(a, b):
    sum = a + b
    difference = abs(a - b)
    if a == b or sum == 5 or difference == 5:
        return True
    else:
        return False

print(sum_of_two(5, 5))
print(sum_of_two(2, 3))
print(sum_of_two(5, 10))
print(sum_of_two(4, 10))