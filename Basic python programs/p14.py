
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print (value)


shipping_label("Dr.","spongebob","squarepants","III",
               street="123 str",
               apt="100",
               city="london",
               state="uutarakhand",
               zip="12345")