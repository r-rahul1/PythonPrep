def b_sort(elements,key):
    l = len(elements)
    for i in range(l-1):
        swapped = False
        for j in range(l-1):
            if elements[j][key] > elements[j+1][key]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    b_sort(elements,'transaction_amount')
    print(elements)