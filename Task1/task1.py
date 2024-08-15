def task1():
    lst = []
    rs = []

    # Thu thap chuoi ma nguoi dung nhap
    a = int(input("Enter array length :"))

    for i in range(0, a):
        n = str(input( "Input something:" ))
        lst.append(n)
    print(lst)

    # Tao 1 mang lay do dai cac chuoi trong mang co san
    lengths = [len(x) for x in lst]
    print("The string lengths are:", lengths)

    # Kiem tra chuoi co do dai xuat hien nhieu nhat trong mang
    most_frequent = lengths.count(max(lengths))

    # Dua nhung chuoi co do dai xuat hien nhieu nhat trong mang vao mot mang trong da khoi tao (rs)
    for i in lst:
        if len(i) == most_frequent:
            rs.append(i)
    print("The most frequent length is:",+ most_frequent)
    print("Corresponding to: ", rs)
task1()