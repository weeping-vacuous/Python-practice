class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
     

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node= Node(data)
        if not self.head:
            new_node.next=self.head
            if self.head:
                self.head.prev=new_node
            self.head=new_node    
            return
        
        last_node = self.head    
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        new_node.prev=last_node

    def inset_at_position(self,data,pos):
        new_node=Node(data)
        temp=self.head
        if pos == 1:
            new_node.next=self.head
            if self.head:
                self.head.prev=new_node
            self.head=new_node    
            return
        else :
            curr_node=temp
            curr_pos=1
            while curr_pos<pos-1 and curr_node:
                curr_node=curr_node.next
                curr_pos+=1
            if not curr_node:
                print("position out of bounds.")

            
            new_node.next=curr_node.next
            if new_node.next:
                new_node.next.prev=new_node
            curr_node.next=new_node
            new_node.prev=curr_node
                     
    def display(self):
        temp=self.head
        if not temp:
            print("List Empty. Please create a list before displaying it.")
            return
        while temp:
            print(f"{temp.data} ->",end=" ")
            temp=temp.next
        else: print("End")    
        
    def delete(self,pos):
        temp=self.head
        if not self.head:
            print("Empty List")
        elif pos==1:
            if self.head.next:
                self.head=self.head.next
                self.head.prev=None
        else :
            curr_node=temp
            curr_pos=1
            while curr_pos<pos and curr_node:
                curr_node=curr_node.next
                curr_pos+=1
            if not curr_node:
                print("position out of bounds.")
        curr_node.prev.next=curr_node.next
        if curr_node.next:
            curr_node.next.prev = curr_node.prev       

    def reversed(self):
        temp=self.head
        if not temp:
            print("List Empty. Please create a list before displaying it.")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(f"{temp.data} ->",end=" ")
            temp=temp.prev
        else: print("End")    

ch=None
List=Linkedlist()
while ch!="f":
    ch=input("Enter the action to be performed(a,b,c):\n(a)Append list\n(b)Display list\n(c)Insert At a position\n(d)Print Reverse\n(e)Delete\n(f)Quit\n").lower()
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
            print("Reversed of the list is:")
            List.reversed() 
        case "e":
            pos=int(input("Enter the postion whizh you want to delete: "))
            List.delete(pos)  
        case "f":
            print("Quiting..")
        case _:
            print("Invalid Input..")

  