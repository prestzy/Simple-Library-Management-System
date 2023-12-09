# Simple-Library-Management-System
Sunway University Computer Science Year 1 Sem 1 Final Project

1.0 Assignment Description 
a) Assignment Scenario 
As a book enthusiast, you have amassed a huge number of physical books in your personal library over the years that span across various literary genres. With your newfound knowledge of Python programming, 
you would like to use it to keep track of all the books in your collection. Hence, the main aim of this programming project is to develop a personal book management system using the Python 3 programming language.

2.0 Programming Requirements 
a) Initial Data Preparation The book management system will require you to prepare a text file containing all the initial data. 
• books_StudentID.txt - Contains initial data of at least 20 initial book information. The information that should be tracked within the book management system is the ISBN, author, title, publisher, genre, year published, 
  date_purchased, and status. The information stored within the text file acts like a database containing all the book information. 
  
b) Program Functionality 
• The book management system developed should provide the user with a menu of action items that could be executed repeatedly until the user explicitly chooses to ‘Exit’ the program. The options that should be provided to the 
user in the form of a main menu are as follows: 

  (a) Add Book Record(s) 
      • Add book information(s) into the system.
      • Within this submenu, the user must be able to add information of single/multiple books.
      
  (b) Delete Book Record(s)    
      • Delete book information(s) in the system.  
      • Within this submenu, the user must be able to delete information of single/multiple books. 
      
  (c) Update/Edit Book Record(s) 
      • Prompts the user for the ISBN or author and title.  
      • If there are matching records found, prompt the user to enter the new information for the book. 
      • Update the book record(s) according to the new information provided.  
      • Within this submenu, the user must be able to update information of single/multiple books

  (d) Display  
      • Display all the books that are currently in the system. 
      • The display should contain appropriate headings for each column. 
      • Data from books_StudentID.txt must be read and stored in the program when the program first runs so that all the book information previously stored in the text file will be displayed 
        if it is the first option selected when starting the program. 

  (e) Search for Book(s) 
      • Prompts for the ISBN, author, and title. 
      • Display the information of a particular book using the information provided. 
      
  (f) Exit  
      • Stop the execution of the program.  
      • The program will write the updated data into books_StudentID.txt. 
