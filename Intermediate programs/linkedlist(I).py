class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
     

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node= Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node = self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    
    def display(self):
        temp=self.head
        while True:
            print(f"{temp.data} ->",end=" ")
            if not temp.next:
                print("End")    
                break
            temp=temp.next

ch=None
List=Linkedlist()
while ch!="c":
    ch=input("Enter the action to be performed(a,b,c):\n(a)Append list\n(b)Display list\n(c)Quit\n").lower()
    match ch:
        case "a":
            data=input("Enter data to be appended(integers):")
            List.append(data)
        case "b":
            print("Current list is:")
            List.display()
        case "c":
            print("Quiting..")
        case _:
            print("Invalid Input..")

  