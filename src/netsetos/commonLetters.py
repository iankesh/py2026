def common_letters():
    s1 = "NAINA"
    s2 = input("Enter 2nd String") #Case-Sensitive

    a = set()
    set1 = set(s1)
    set2 = set(s2)
    # for s in s1:
    #     if s in s2:
    #         # print(s)
    #         a.add(s)
    # for i in a:
    #     print(i)

    lst = set1 & set2
    print(lst)

common_letters()