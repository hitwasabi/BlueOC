def task2():
    lst = []
    rs = []

    # Thu thap so ma nguoi dung nhap
    a = int(input("Enter array length :"))

    for i in range(0, a):
        n = int(input( "Input something:" ))
        lst.append(n)
    print(lst)

    # Sap xep mang theo thu tu tu lon den be
    lst.sort(reverse=True)
    # Lay 2 phan tu dau tien
    max_int1 = lst[0]
    max_int2 = lst[1]
    print("The two largest integers are:", + max_int1 , "and",+ max_int2)
    # Sum
    sum = max_int1 + max_int2
    print("Their sum is :",+ sum )
task2()


    