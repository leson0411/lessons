reading_list = []

MENU = """
Enter
a - add the book
s - show the book
d - delete the book
f - find a book
q - quit the program
choose option you want: """


def add_the_book():
    title = input("Enter the title of book: ").strip().title()
    author = input("Enter the author of book: ").strip().title()
    release_year = input("Enter the release year of book: ").strip()

    reading_list.append({
        "title": title,
        "author": author,
        "release_year": release_year
    })


def show_book_detail(book):
    print(f"{book['title']} is published by {book['author']} in {book['release_year']}")


def show_books():
    if len(reading_list) == 0:
        print("Reading list is empty")
    else:
        for book in reading_list:
            show_book_detail(book)


def search_the_book():
    if len(reading_list) == 0:
        print("failure")
    else:
        flag = False
        keyword = input("Enter the book you want to search for: ").strip().lower()
        for book in reading_list:
            if keyword in book['title'].lower():
                show_book_detail(book)
                flag = True
        if not flag:
            print("The book is not found!")


def delete_the_book():
    global reading_list
    if len(reading_list) == 0:
        print("failure")
    else:
        deleted = input("Enter the book you want to delete: ").strip().lower()

        reading_list = [
            book
            for book in reading_list
            if deleted not in book['title'].lower()
        ]

        show_books()


operations = {
    'a': add_the_book,
    's': show_books,
    'f': search_the_book,
    'd': delete_the_book
}

while True:
    selected_option = input(MENU).strip()

    if selected_option in operations:
        operations[selected_option]()
    elif selected_option == 'q':
        print("Quitting the menu!")
        break
    else:
        print("The program can not be activated")
