#Magic methods
class Book:

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
 
    def __lt__(self,other):
        return self.pages < other.pages
   
    def __Gt__(self,other):
        return self.pages > other.pages
    
    def __add__(self,other):
        return f"{self.pages + other.pages} pages"
    
    def __contains__(self,key):
        return key in self.title or key in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return "Invalid Key"


book1=Book("The Hobbit","J.R.R. Tolkien",295)
book2=Book("Harry Potter","J.K. Rowling",500)
book3=Book("The lion, the witch and the wardrobe","C.S. Lewis",350)

print(book3["title"] )