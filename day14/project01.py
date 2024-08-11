MENU = """
    Enter
    a - add the book
    s - show the book
    f - find a book
    q - quit the program
    choose option you want: """


def add_the_book():
    title = input("Enter the title of book: ").strip().title()
    author = input("Enter the author of book: ").strip().title()
    release_year = input("Enter the release year of book: ").strip()
    with open("book.csv", "a") as reading_list:
        reading_list.append(f"{title},{author},{release_year}\n")


def get_all_books():
    books = []
    with open("book.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year = book.strip().split(",")

        books.append({"title": title, "author": author, "year": year})


def find_books():
    search = input("Please enter the book title that you are searching for: ").strip().lower()
    matching_book = []
    reading_list = get_all_books()
    for book in reading_list:
        if search in book['title'].lower():
            matching_book.append(book)

    return matching_book

def show_books(books):
    for book in books:
        print(f"{book['title']}, by {book['author']} in {book['year']}")


operations = {
    'a': add_the_book,
    's': show_books,
    'f': find_books,
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
