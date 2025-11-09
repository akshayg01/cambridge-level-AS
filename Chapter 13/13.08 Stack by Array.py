
books = []
def push_book(title, author):
    books.append({'title': title, 'author': author})    
def pop_book():
    if books:
        return books.pop()
    else:
        return None
def peek_book():
    if books:
        return books[-1]
    else:
        return None
def is_empty():
    return len(books) == 0
def stack_size():
    return len(books)
def output_stack():
    for book in reversed(books):
        print(f"Title: {book['title']}, Author: {book['author']}")


# Example usage:push_book("1984", "George Orwell")
push_book("To Kill a Mockingbird", "Harper Lee")
output_stack()
print(peek_book())  # Output: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
output_stack()
push_book("The Great Gatsby", "F. Scott Fitzgerald")        
output_stack()
print(stack_size())  # Output: 2
output_stack()
print(pop_book())    # Output: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
output_stack()
print(is_empty())    # Output: False    