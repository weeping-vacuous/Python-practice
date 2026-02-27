##5
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Store:
    def __init__(self):
        self._products=[]

    def add(self,product):
        if isinstance(product,Product):
            self._products.append(product)
        else:
            print("Only Product type object are allowed.")
    
    def remove_product(self,prod_name):
        product_to_remove=None
        for product in self._products:
            if product.name == prod_name:
                product_to_remove=product
                break
        if product_to_remove:
            self._products.remove(product_to_remove)
            print(f"{product_to_remove.name} has been removed.")
        else:
            print("No such product in store")
    
    def sell(self,prod_name,Qty):
        for product in self._products:
            if product.name==prod_name:
                if product.quantity>=Qty:
                    product.quantity-=Qty
                    print(f"The total price for your purchase of {Qty} {product.name}is: {Qty*product.price}")
                    print("--------------------------------------------------")
                    break
                else:
                    print("Not enough Quantity")
                    print("--------------------------------------------------")   
                    break
        else:
            print("Product not found") 


    def show_products(self):
        for product in self._products:
            print("--------------------------------------------------")
            print(f"Product Name: {product.name:8}   Product price: {product.price:8}  Product Qty: {product.quantity:8}")
        else:
            print("--------------------------------------------------")    

            
general_store=Store()

product=Product("Shampoo",5.99,100)
product1=Product("Soap",1.99,87)
product2=Product("Stool",2.99,25)
product3=Product("Table",19.99,13)
product4=Product("Chair",29.99,10)
product5=Product("Basket",.99,125)
general_store.add(product)
general_store.add(product1)
general_store.add(product2)
general_store.add(product3)
general_store.add(product4)
general_store.add(product5)

if __name__ =="__main__":
    print("------------Welcome to General Store-------------")
    while True:
        choice=input("What actions do you want to perform(type a,b,c,d,q to exit)\nA. Show available products\nB. Add new product\nC. Remove a product\nD. Sell a product\n").lower()
        print("--------------------------------------------------")
        match choice:
            case 'a':
                general_store.show_products()
            case 'b':
                data_string=input("Enter product name, price and quantity (separated by space): ")
                name,price,qty = data_string.split()
                price=float(price)
                qty=int(qty)
                new_product=Product(name,price,qty)
                general_store.add(new_product)
            case 'c':
                prodname=input("Enter the product name: ")
                general_store.remove_product(prodname)
            case 'd':
                data_string2=input("Enter the product you want to sell and its quantity(seprated by space): ")
                name1,qty1=data_string2.split()
                qty1=int(qty1)
                general_store.sell(name1,qty1)
            case 'q':
                print("Exiting the program")
                break
            case _:
                print("Inavalid input")



    