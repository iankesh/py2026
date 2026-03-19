def missing_elements_by_summation(a):
    n = a[-1]
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)

# def missing_element_by_xor(a):
#     for i in range(1,len(a)):
#


a = [1,2,4,5,6,7]
missing_elements_by_summation(a)