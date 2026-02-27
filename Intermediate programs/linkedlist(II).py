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

    def inset_at_position(self,data,pos):
        new_node=Node(data)
        temp=self.head
        if pos == 1:
            self.head=new_node
            new_node.next=temp
        else :
            curr_node=temp
            curr_pos=1
            while curr_pos<pos-1 and curr_node:
                curr_node=curr_node.next
                curr_pos+=1
            if not curr_node:
                print("position out of bounds.")

            new_node.next=curr_node.next
            curr_node.next=new_node    
        
     
    def display(self):
        temp=self.head
        if not temp:
            print("List Empty. Please create a list before displaying it.")
            return
        while True:
            print(f"{temp.data} ->",end=" ")
            if not temp.next:
                print("End")    
                break
            temp=temp.next

ch=None
List=Linkedlist()
while ch!="d":
    ch=input("Enter the action to be performed(a,b,c):\n(a)Append list\n(b)Display list\n(c)Insert At a position\n(d)Quit\n").lower()
    match ch:
        case "a":
            data=input("Enter data to be appended:")
            List.append(data)
        case "b":
            print("Current list is:")
            List.display()
        case "c":
            pos,data=input("Enter the position and data to be inserted seperated by spaces: ").split()
            pos=int(pos)
            List.inset_at_position(data,pos)    
        case "d":
            print("Quiting..")
        case _:
            print("Invalid Input..")

  