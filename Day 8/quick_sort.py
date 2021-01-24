def quickSort(arr):
    if len(arr) == 1:
        return arr
    smaller, larger, p = divide(arr)
    if len(smaller) > 1:
        smaller = quickSort(smaller)
    if len(larger) > 1:
        larger = quickSort(larger)
    print(smaller + [p] + larger)
    return smaller + [p] + larger
    
def divide(arr):
    p = arr[0]
    smaller = []
    larger = []
    for i in arr:
        if i > p:
            larger.append(i)
        elif i < p:
            smaller.append(i)
    return smaller, larger, p