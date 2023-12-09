def Add_Book():
    '''
    This function task is to add new book's informations into book list
    Function: Using the info provided by users, added into text file
    '''
    try:
        with open("Assignment\\books_StudentID.txt", 'a') as f: # Access the text file

            # Ask if user would like to go back to Main Menu?
            back = input ("press 'q' if you would like to return or \n" +
                            "Enter any other alphabet if you would like to continue: ")
            if back.lower() == 'q':
                main()
            else:
                # Prompt user to input the book information
                isbn = input("\nEnter ISBN: ")
                author = input("Enter author: ")
                title = input("Enter title: ")
                publisher = input("Enter publisher: ")
                genre = input("Enter genre: ")
                year_published = input("Enter year published: ")
                date_purchased = input("Enter date purchased: ")
                status = input("Enter status (read/to-read): ")

                # Construct book information
                book_info = f"{isbn}, {author}, {title}, {publisher}, {genre}, {year_published}, {date_purchased}, {status}"

                # Write the book information to the file
                f.write(book_info + '\n')

                print("Book added successfully!")

    except Exception as e:
        print(e, "Please try again! ")
        return
    


def Delete_Book():
    ''' 
    This function is for User to delete the book with ISBN
    Function: rewrite every book until it reaches the matched isbn, skip it and continue writing others. 
    '''
    try:
        # Ask if user would like to go back to Main Menu?
        back = input ("press 'q' if you would like to return or \n" +
                        "Enter any other alphabet if you would like to continue: ")
        
        if back.lower() == 'q':
            main()

        else:
            book_isbn = input("What is the book's isbn?: ")

            with open("Assignment\\books_StudentID.txt", "r") as f: # Read the file, assigned as variable 'f'
                lines = f.readlines()

            with open("Assignment\\books_StudentID.txt", "w") as f:
                book_found = False  # Flag is True when matching book is found

                #iterate every line in the lines
                for line in lines:
                    # Split the String into List to extract the ISBN
                    parts = line.split(',')
                    line_isbn = parts[0].strip()  

                    if book_isbn == line_isbn:
                        book_found = True
                    else:
                        f.write(line)

                # Print statement depends on True or False
                if book_found:
                    print("\nBook deleted successfully!")
                else:
                    print("\nNo matching book found. Deletion failed.")

    except FileNotFoundError:
         print("File 'Assignment\\books_StudentID.txt' not found.")
         return
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        return



def Edit_Book():
    '''
    This function is for the user to edit the book's ISBN or author and title.
    Function: Rewrite the booklist; if isbn/author and title matched, use the replace function to change the old one to the new one.
    '''
    # Ask if the user would like to return to the Main Menu
    back = input("Press 'q' if you would like to return or \n" +
                 "Enter any other alphabet if you would like to continue: ")

    if back.lower() == 'q':
        main()
    else:
        # Repeat the question if the user enters other than 1 and 2
        while True:
            choice = input("Please enter '1' for editing ISBN or '2' for editing author and title: ")
            if choice == '1' or choice == '2':
                break
            else:
                print("Please enter a valid number!")

        if choice == '1':
            # Ask the user to input the new and old ISBN
            old_isbn = input("Enter the ISBN of the book you would like to edit: ")
            new_isbn = input("Enter the new ISBN for the book: ")

            # Check format for isbn
            if not old_isbn.isdigit() or not new_isbn.isdigit():
                print("Invalid ISBN format. Please enter numeric values.")
            else:
                try:
                    # Read the text file
                    with open("Assignment\\books_StudentID.txt", 'r') as f:
                        lines = f.readlines()

                    # Write the text file
                    with open("Assignment\\books_StudentID.txt", 'w') as f:
                        book_found = False  # Set default Flag as false

                        for line in lines:
                            parts = line.split(',')  # Using split function to split string into a list
                            line_isbn = parts[0].strip()

                            if old_isbn == line_isbn:
                                line = line.replace(old_isbn, new_isbn)  # Replace old with new ISBN
                                book_found = True  # Set Flag as True

                            f.write(line)  # Continue writing the remaining lines

                        if book_found:
                            print("ISBN edited successfully")
                        else:
                            print("Book not found")

                except FileNotFoundError as x:
                    print(f"Error: {x}. Please check your file path")

        elif choice == '2':
            # Ask the user to enter the old and new author and title
            old_author_title = input("Enter the author and title of the book you want to edit (format: Preston, Me in wonderland): ")
            new_author = input("Enter the new author's name: ")
            new_title = input("Enter the new book's title: ")

            # Check author and title format
            if ',' not in old_author_title or ',' not in f"{new_author},{new_title}":
                print("Invalid author/title format. Please use the format: Author,Title.")
            else:
                try:
                    with open("Assignment\\books_StudentID.txt", 'r') as f:
                        lines = f.readlines()

                    with open("Assignment\\books_StudentID.txt", 'w') as f:
                        book_found = False

                        for line in lines:
                            parts = line.split(',')  # divide the string into parts with a comma
                            line_author_title = f"{parts[1].strip()},{parts[2].strip()}"  # using strip to remove the excess spaces

                            if old_author_title == line_author_title:
                                line = line.replace(parts[1].strip(), new_author)   # Replace the old with new one
                                line = line.replace(parts[2].strip(), new_title)
                                book_found = True   # Set Flag to True

                            f.write(line) # Rewrite back the book list

                        # Tell the user if the books edited successfully or not
                        if book_found:
                            print("Author and title edited successfully")
                        else:
                            print("Book not found")

                except FileNotFoundError as x:
                    print(f"Error: {x}. Please check your file path")

        else:
            print("Invalid Choice, Please Enter '1' or '2'")
 

            
def Display_Book():
    all_books = []
    # Reading books from file
    filename = "Assignment\\books_StudentID.txt"
    try:
        with open(filename, 'r') as f:
            for line in f:
                book_data = line.strip().split(',')
                all_books.append(book_data)

    except FileNotFoundError:
        # Handle when the file is not found
        print(f"File '{filename}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")

    # If no book in all_book list, print
    if not all_books: 
        print("No books found.")
        return

    # Print column headings
    headings = ["ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
    print("{:<17}{:<25}{:<34}{:<20}{:<10}{:<13}{:<15}{:<10}".format(*headings)) # '<' left = alignment, *headings = unpack the heading list

    for book in all_books:
        # Print each book's information
        book_info = [
            book[0].strip(),
            book[1].strip(),
            book[2].strip(),
            book[3].strip(),
            book[4].strip(),
            book[5].strip(),
            book[6].strip(),
            book[7].strip()
        ]
        print("{:<17}{:<25}{:<34}{:<20}{:<15}{:<10}{:<15}{:<10}".format(*book_info)) # print the info of book



def Search_Book():
    # Prompt user if he wants to go back to main menu
    back = input ("press 'q' if you would like to return or \n" +
                            "Enter any other alphabet if you would like to continue: ")
    if back.lower() == 'q':
        main()
    else:
        # Prompt user to enter their choice
        print("Enter '1' for book's ISBN\n Enter '2' for book's author\n Enter '3' for book's title")
        try:
            choice = int(input("Please enter your choice: "))
        except Exception as e:  # Raise error if is not numerical number/valid option
            print(f"Error:{e}. Please enter a valid option (1/2/3)")
            return

        if choice == 1:
            isbn = input("Please enter the book's ISBN (no space allowed): ")

            with open("Assignment\\books_StudentID.txt", 'r') as f:
                lines = f.readlines()

            book_found = False     # Set Flag default to False

            # Starts the iterate the line in text file
            for line in lines: 
                parts = line.split(',')    # Separate string to list
                line_isbn = parts[0].strip()    # assign every index 0(isbn) to new var

                # Compare the isbn 
                if isbn.lower() == line_isbn.lower(): 
                    book_info = (
                        f"\nISBN: {parts[0].strip()}"
                        f"\nAuthor: {parts[1].strip()}"
                        f"\nTitle: {parts[2].strip()}"
                        f"\nPublisher: {parts[3].strip()}"
                        f"\nGenre: {parts[4].strip()}"
                        f"\nYear Published: {parts[5].strip()}"
                        f"\nDate Purchased: {parts[6].strip()}"
                        f"\nStatus: {parts[7].strip()}"
                    )
                    print(book_info)
                    book_found = True   # print book info and set to True

            # If book_found is False, print statement
            if not book_found:
                print("No matching book found.")

        elif choice == 2:
            # Prompt user enters author's name
            author = input("Please enter the author's name: ") 

            with open("Assignment\\books_StudentID.txt", 'r') as f:
                lines = f.readlines()

            book_found = False 

            # Start iteration
            for line in lines: 
                parts = line.split(',')
                line_author = parts[1].strip()

                # Set everything as lowercase
                if author.lower() == line_author.lower():   
                    # Set the book info
                    book_info = (
                        f"\nISBN: {parts[0].strip()}"
                        f"\nAuthor: {parts[1].strip()}"
                        f"\nTitle: {parts[2].strip()}"
                        f"\nPublisher: {parts[3].strip()}"
                        f"\nGenre: {parts[4].strip()}"
                        f"\nYear Published: {parts[5].strip()}"
                        f"\nDate Purchased: {parts[6].strip()}"
                        f"\nStatus: {parts[7].strip()}"
                    )
                    print(book_info)    # Print the book_info
                    book_found = True

            # if no matching book, print statement
            if not book_found: 
                print("No matching book found.")

        elif choice == 3:
            title = input("Please enter the book's title: ")

            with open("Assignment\\books_StudentID.txt", 'r') as f:
                lines = f.readlines()

            book_found = False

            # Starts iteration
            for line in lines:
                parts = line.split(',')
                line_title = parts[2].strip()

                if title.lower() == line_title.lower(): # Set into lowercase
                    # Set the format for book_info
                    book_info = (
                        f"\nISBN: {parts[0].strip()}"
                        f"\nAuthor: {parts[1].strip()}"
                        f"\nTitle: {parts[2].strip()}"
                        f"\nPublisher: {parts[3].strip()}"
                        f"\nGenre: {parts[4].strip()}"
                        f"\nYear Published: {parts[5].strip()}"
                        f"\nDate Purchased: {parts[6].strip()}"
                        f"\nStatus: {parts[7].strip()}"
                    )
                    print(book_info)
                    book_found = True

            # if no matching book, print statement
            if not book_found: 
                print("No matching book found.")

        else:
            print("Invalid Option")

                            

def main():
    all_books = []

    # Reading books from file
    filename = "Assignment\\books_StudentID.txt"
    
    # Exception Handling
    try:
        with open(filename, 'r') as f:
            for line in f:
                book_data = line.strip().split(',')
                all_books.append(book_data)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except Exception as e:
        print(f"Error occurred: {e}")
        return

    # Print Options for user
    while True: 
        print("\nOptions:")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. Edit a Book")
        print("4. Display All Books")
        print("5. Search for a Book")
        print("6. Exit")

        # Prompt user to input the choice
        choice = input("Enter your choice (1-6): ")

        # Execute the function with user choice
        if choice == '1':
            Add_Book()

        elif choice == '2':
            Delete_Book()

        elif choice == '3':
            Edit_Book()

        elif choice == '4':
            Display_Book()

        elif choice == '5':
            Search_Book()

        elif choice == '6':
            print("Bye Bye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Execute the main function
if __name__ == "__main__":
    main()


