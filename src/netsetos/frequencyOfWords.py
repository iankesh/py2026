def freq_words():
    str = "Sheena loves eating mango and apple . Her sister also loves eating mango and apple"
    lst = str.split()
    print(lst)
    d = {}
    for i in lst:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)

freq_words()