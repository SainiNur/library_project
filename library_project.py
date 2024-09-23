Book_database = {
    'A001': {'Title': 'Administrasi Pembangunan', 'Stock': 25, 'Publisher': 'Bumi Aksara', 'Year': 2009, 'Type': 'Book', 'Location': 'ADMINISTRASI'},
    'A002': {'Title': 'Administrasi Perkantoran', 'Stock': 9, 'Publisher': 'Gramedia', 'Year': 2010, 'Type': 'Thesis', 'Location': 'ADMINISTRASI'},
    'A003': {'Title': 'Administrasi Publik', 'Stock': 16, 'Publisher': 'Salemba Aksara', 'Year': 2015, 'Type': 'Book', 'Location': 'ADMINISTRASI'},
    'IG001': {'Title': 'Ilmu Gizi', 'Stock': 7, 'Publisher': 'Dian Rakyat', 'Year': 2006, 'Type': 'Thesis', 'Location': 'ILMU GIZI'},
    'IG002': {'Title': 'Ilmu Gizi Keperawatan & Kesehatan', 'Stock': 14, 'Publisher': 'Nuha Medika', 'Year': 2011, 'Type': 'Journal', 'Location': 'ILMU GIZI'},
    'IG003': {'Title': 'Ilmu Gizi Untuk Mahasiswa', 'Stock': 18, 'Publisher': 'Dian Rakyat', 'Year': 2006, 'Type': 'Journal', 'Location': 'ILMU GIZI'},
    'M001': {'Title': 'Manajemen Administrasi', 'Stock': 2, 'Publisher': 'Ui Press', 'Year': 2012, 'Type': 'Thesis', 'Location': 'MANAJEMEN'},
    'M002': {'Title': 'Manajemen Kesehatan', 'Stock': 7, 'Publisher': 'Gramedia', 'Year': 2013, 'Type': 'Book', 'Location': 'MANAJEMEN'},
    'M003': {'Title': 'Manajemen Kinerja', 'Stock': 2, 'Publisher': 'Ui Press', 'Year': 2012, 'Type': 'Thesis', 'Location': 'MANAJEMEN'},
    'S001': {'Title': 'Solusi Statistik SPSS', 'Stock': 9, 'Publisher': 'Elex Media', 'Year': 2008, 'Type': 'Book', 'Location': 'STATISTIK'},
    'S002': {'Title': 'Statistik Rumah Sakit', 'Stock': 8, 'Publisher': 'Graha Ilmu', 'Year': 2010, 'Type': 'Book', 'Location': 'STATISTIK'},
    'M004': {'Title': 'Analisis Karyawan PT.ABC', 'Stock': 2, 'Publisher': 'Bn Press', 'Year': 2009, 'Type': 'Thesis', 'Location': 'MANAJEMEN'},
    'IG004': {'Title': 'Analisa Biaya Pelayanan Klinik ABC', 'Stock': 2, 'Publisher': 'Bn press', 'Year': 2012, 'Type': 'Thesis', 'Location': 'ILMU GIZI'},
    'P001': {'Title': 'Psikologi Kesehatan', 'Stock': 14, 'Publisher': 'Mitra Cendikia', 'Year': 2008, 'Type': 'Book', 'Location': 'PSIKOLOGI'},
    'P002': {'Title': 'Psikologi Perkembangan Anak', 'Stock': 7, 'Publisher': 'Palmall', 'Year': 2016, 'Type': 'Book', 'Location': 'PSIKOLOGI'},
    'S003': {'Title': 'Manajemen Data Analisis', 'Stock': 6, 'Publisher': 'Alfabeta', 'Year': 2015, 'Type': 'Book', 'Location': 'STATISTIK'},
    'K001': {'Title': 'Analisis Pelaksanaan Pelayanan RS.XYZ', 'Stock': 2, 'Publisher': 'Bn press', 'Year': 2015, 'Type': 'Thesis', 'Location': 'KESEHATAN'},
    'K002': {'Title': 'Hubungan Tinggi & Berat Anak', 'Stock': 2, 'Publisher': 'Ui Press', 'Year': 2013, 'Type': 'Thesis', 'Location': 'KESEHATAN'},
    'K003': {'Title': 'Penanganan Pasien AIDS', 'Stock': 12, 'Publisher': 'Gramedia', 'Year': 2014, 'Type': 'Book', 'Location': 'KESEHATAN'},
    'K004': {'Title': 'Metode Penyembuhan Anak', 'Stock': 15, 'Publisher': 'Baca', 'Year': 2009, 'Type': 'Book', 'Location': 'KESEHATAN'}
}

print("="*10,"Welcome to Cendekiawan Library","="*10)

def display_admin():
    while True:
        print("Display option: ")
        print("1. Sort by stock.")
        print("2. Sort by type.")

        option = int(input("Choose display: ")) 

        result = []
        for code, books in Book_database.items():
            result.append([code,books["Title"],books["Stock"],books["Publisher"],books["Year"],books["Type"],books["Location"]])

        if option == 1:
            result.sort(key = lambda x: x[2])
        elif option == 2:
            result.sort(key = lambda x: x[5])
        else:
            print('Invalid option')
            break

        print("\nBooks database")
        print(f"\n{'Code':<6} | {'Title':<40} | {'Stock':<5} | {'Publisher':<20} | {'Year':<6} | {'Type':<10} | {'Location':<15}") # Header
        print('-' * 110) # Separator
        for book in result:
            print(f"{book[0]:<6} | {book[1]:<40} |{book[2]:^6} | {book[3]:<20} | {book[4]:<6} |{book[5]:<10} | {book[6]:<15}")

        next_stop = str(input("\nDo you want to continue  books? y/n: "))
        if next_stop.lower() == "n":
            break

def add_books_adm():
    
    while True: 
        no_series = str(input("\nInsert book ID: ")).upper()
        title_ = str(input("Insert book title: ")).capitalize()
        stock_ = int(input("Insert book stock: "))
        publisher_ = str(input("Insert book publisher: ")).capitalize()
        year_ = int(input("Insert book year: "))
        type_ = input("Insert book type: ").capitalize()
        location_ = str(input("Insert book rack: ")).upper()
        
        for code, detail in list(Book_database.items()):
            if no_series == code: 
                print(f"The book with title {title_} is exist.")
                break
        else:
            Book_database[no_series] = {"Title":title_, "Stock":stock_, "Publisher":publisher_, "Year":year_,"Type":type_,"Location":location_}
            print(f"Books with title {title_} and number series {no_series} successfully added!")

        print("\nBooks database")
        print(f"\n{'Code':<6} | {'Title':<40} | {'Stock':<5} | {'Publisher':<20} | {'Year':<6} | {'Type':<10} | {'Location':<15}") # Header
        print('-' * 110) 
        for kode, book in Book_database.items():
            print(f"{kode:<6} | {book['Title']:<40} | {book['Stock']:<5} | {book['Publisher']:<20} | {book['Year']:<6} | {book['Type']:<10} | {book['Location']:<15}")

        next_stop = str(input("\nDo you want to continue adding books? y/n:" ))
        if next_stop.lower() == "n":
            break

def remove_adm():
    while True:
        print("\nBooks database")
        print(f"\n{'Code':<6} | {'Title':<40} | {'Stock':<5} | {'Publisher':<20} | {'Year':<6} | {'Type':<10} | {'Location':<15}") # Header
        print('-' * 110) # Separator
        for kode, book in Book_database.items():
            print(f"{kode:<6} | {book['Title']:<40} | {book['Stock']:<5} | {book['Publisher']:<20} | {book['Year']:<6} | {book['Type']:<10} | {book['Location']:<15}")
        
        name_to_remove = str(input("\nEnter the book name you want to remove(press 'cancel' to go back): "))
        if name_to_remove.lower() == "cancel":
            print("Deletion canceled")
            break
        code_remove = str(input("Enter the book code you want to remove: ")).upper()
        for code,book in list(Book_database.items()):
            if code == code_remove:
                removed_book = Book_database.pop(code)
                print(f"{name_to_remove} has been removed.")
                break
        else:
            print("Book detail is not matched with database")

        next_stop = str(input("Do you want to continue remove books? y/n:" ))
        if next_stop.lower() == "n":
            break

def display_visitors():

    while True:
        print("\nDisplay by: ")
        print("\t1.Book name")
        print("\t2.Publisher ")
        print("\t3.Show collection ")

        display_option = int(input("\nEnter display option: "))

        if display_option == 1: # By name
            display_result = []
            
            book_name = str(input("Input book title that you want: "))
            # Searching book
            for code, detail in list(Book_database.items()):
                if book_name.lower() in detail["Title"].lower():
                    display_result.append({code: detail})

            #Show result
            if display_result:
                print("Search result: ")
                print(f"\n{'Title':<40} | {'Stock':<5} | {'Publisher':<20} | {'Year':<6} | {'Type':<10} | {'Location':<15}") # Header
                print('-' * 110) # Separator
                for books in display_result:
                    for code,detail in books.items():
                        print(f"{detail['Title']:<40} | {detail['Stock']:<5} | {detail['Publisher']:<20} | {detail['Year']:<6} | {detail['Type']:<10} | {detail['Location']:<15}")
                        break
            else:
                print("Book name not found.")

            next_stop = str(input("\nDo you want to continue searching books? y/n:" ))
            if next_stop.lower() == "n":
                break

        elif display_option == 2: # By Publisher
            publisher_result = []

            publisher_name = input("Input publisher name: ")
            for code, books_detail in Book_database.items():
                if publisher_name.lower() in books_detail["Publisher"].lower():
                    publisher_result.append({code: books_detail})
            # Menampilkan hasil pencarian
            if publisher_result:
                print("Search result: ")
                print(f"\n{'Publisher':<20} | {'Title':<40} | {'Stock':<5} |  {'Year':<6} | {'Type':<10} | {'Location':<15}") # Header
                print('-' * 110) 
                for books in publisher_result:
                    for code,detail in books.items():
                        print(f"{detail['Publisher']:<20} | {detail['Title']:<40} | {detail['Stock']:<5} | {detail['Year']:<6} | {detail['Type']:<10} | {detail['Location']:<15}")
                        break
            else:
                print("Book publisher not found.")

            next_stop = str(input("Do you want to continue searching books? y/n:" ))
            if next_stop.lower() == "n":
                break

        elif display_option == 3: # Display all collection

            type_count = {}

            #melihat total koleksi
            for book_info in Book_database.values():
                typ = book_info["Type"]
                if typ not in type_count:
                    type_count[typ] = 0
                type_count[typ] += 1

            print("\nBooks collection")
            print(f"{"Categories": <10} | {"Result":^10}|")
            for typ,count in type_count.items():
                print(f"{typ: <10} | {count:^10}|")
        else:
            print("Invalid display categories.")
        next_stop = str(input("Do you want to continue searching books? y/n:" ))
        if next_stop.lower() == "n":
            break

def borrow():
    book_cart = {}

    visitor_name = str(input("Insert your name: "))
    print(f"\nWelcome {visitor_name}!")

    while True: 
        print("Current Cart:")
        print(f"{'Title':<40} | {'Publisher':<20} | {'Quantity':<5}")
        for detail in book_cart.values():
            title, publisher, qty = detail
            print(f"{title:<40} | {publisher:<20} | {qty:<5}")

        title = input("Insert book title: ").capitalize()
        publisher = input("Insert publisher name: ").capitalize()

        for book_code, details in Book_database.items():
            if details["Title"].lower() == title.lower() and details["Publisher"].lower() == publisher.lower():
                print(f"Book found: {details['Title']} by {details['Publisher']}. Stock available: {details['Stock']}")
                qty = int(input("Insert quantity to add to cart: "))
                
                if qty <= details['Stock']:
                    book_cart[book_code] = [details['Title'], details['Publisher'], qty]
                    Book_database[book_code]['Stock'] -= qty
                else:
                    print("Sorry, not enough book available.")
                break
                    
        else:
            print("book not found")
        
        next_stop = str(input("Do you want to continue borrow books? y/n: "))
        if next_stop.lower() == "n":
            break

    print("\n--- Checkout ---")
    total_books = 0

    # show cart
    print(f"{'Book Code':<6} | {'Title':<40} | {'Publisher':<20} | {'Quantity':<5}")
    for book_code, detail in book_cart.items():
        title, publisher, qty = detail
        print(f"{book_code:<6} | {title:<40} | {publisher:<20} | {qty:<5}")
        total_books += qty

    # Confirmation
    confirm_checkout = input(f"\nYou have {total_books} books in your cart. Do you want to proceed with checkout? (y/n): ").lower()
    if confirm_checkout == 'y':
        print("\nThank you for your purchase! Here is a summary of your order:")
        print(f"{'Book Code':<6} | {'Title':<40} | {'Publisher':<20} | {'Quantity':<5}")
        for book_code, detail in book_cart.items():
            title, publisher, qty = detail
            print(f"{book_code:<6} | {title:<40} | {publisher:<20} | {qty:<5}")
        
        print(f"\nTotal books borrowed: {total_books}")
    else:
        print("\nCheckout canceled. You can continue shopping if you'd like.")
        
    print("\nThank you for visiting our library!")
    

def return_book():
    visitor_name = str(input("Insert your name: "))

    while True: 
        print("\nEnter your books information: ")

        title = str(input("Enter book title: "))
        publisher = str(input("Enter book publisher: "))
        amount = int(input("Enter book amount: "))

        for book_code, details in Book_database.items():
            if details["Title"].lower()==title.lower() and details["Publisher"].lower()==publisher.lower():
                details["Stock"] += amount
                print("Return success!")
                break
        else:
            print("Invalid book data.")

        next_stop = str(input("Do you want to continue returning books? y/n:" ))
        if next_stop.lower() == "n":
            break

def main(): #Main menu
    counter = 0
    while counter != 3:

        print("\nUsers category: ")
        print("1. ADMIN ")
        print("2. VISITORS ")
        print("3. EXIT PROGRAM ")

        Role = (input("Select your user category: "))

        if Role == "1": # ADMIN MENU
            while True:
                print("\nMain Menu:")
                print("1. Display Books Collection ")
                print("2. Add Books Collection")
                print("3. Remove Books Collection")
                print("4. Exit program")

                option = int(input("Enter the menu number you want to run: "))
            
                if option == 1: # Display books
                    display_admin()
                elif option == 2: #Add books
                    add_books_adm()
                elif option == 3: #Remove books
                    remove_adm()
                elif option == 4: #Exit program
                    print("Thank you for visiting us!!!")
                    break
                else:
                    print("Invalid option, please re-entry a valid option.")
            
        elif Role == "2": # VISITORS MENU
            while True:
                print("\nMain Menu:")
                print("1. Display Books Collection ")
                print("2. Borrow Books")
                print("3. Return Books")
                print("4. Exit Program")

                option = int(input("Enter the menu number you want to run: "))

                if option == 1: #Display books
                    display_visitors()
                elif option == 2: #Borrow books
                    borrow()
                elif option == 3: #Return books
                    return_book()
                elif option == 4: #Exit program
                    print("\nThank you for visiting our library!")
                    break
                else:
                    print("invalid menu")
        elif Role == "3": #Exit main menu
            print("Thank you!")
            break
        else:
            counter += 1
            print(f"Invalid role category, error attempt {counter}/3!")
main()