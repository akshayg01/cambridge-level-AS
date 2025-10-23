# TASK 13.02
# Write the declaration of a record type to store the details of a book: Title, Year of publication,
# Price, ISBN.

# Write the statements required to assign the values “Computer Science”, 2019, £44.95,
# “9781108733755” to the fields respectively.

# Task 13.07
# Declare an array of BookType (see Task 13.02) for 200 books.
# Set the first book’s details to the values given in Task 13.02.


book = { "Title" : "Computer Science", 
        "Year_of_publication" : 2019 , 
         "Price" : 44.95 , 
         "ISBN" : "9781108733755" 
           }

books = []
books.append(book)
print(books)

file_object = open('D:\\workspace\\cambridge-level-AS\\Chapter 13\\books.txt', 'a')
file_object.write(str(books))
file_object.close()

# HW Write pseudocode to read the values stored in the text file back into the board array.

