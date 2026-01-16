import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="134.209.101.105",
        user="group32",
        password="password32",
        database="db_group32"
    )
def insert_movie():
    db = connect_db()
    cursor = db.cursor()

    movie_id = input("Enter Movie ID: ")
    movie_name = input("Enter Movie Name: ")
    movie_genre = input("Enter Movie Genre: ")
    movie_length = input("Enter Movie Length (in minutes ex 160 min): ")

    try:
        cursor.execute("INSERT INTO Movie (MovieID, MovieName, MovieGenre, MovieLength) VALUES (%s, %s, %s, %s)",
                       (movie_id, movie_name, movie_genre, movie_length))
        db.commit()
        print("Movie added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    cursor.close()
    db.close()

def insert_customer():
    db = connect_db()
    cursor = db.cursor()

    customer_id = int(input("Enter Customer ID: "))
    customer_name = input("Enter Customer Name: ")
    seat_number = input("Enter Seat Number: ")

    try:
        cursor.execute("INSERT INTO Customer (CustomerID, Name, SeatNumber) VALUES (%s, %s, %s)",
                       (customer_id, customer_name, seat_number))
        db.commit()
        print("Customer added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    cursor.close()
    db.close()

def select_with_join():
    db = connect_db()
    cursor = db.cursor()

    query = """
    SELECT Booking.BookingID, Ticket.TicketID, Cinema.CinemaID, Movie.MovieName
    FROM Booking
    JOIN Ticket ON Booking.TicketID = Ticket.TicketID
    JOIN Cinema ON Ticket.CinemaID = Cinema.CinemaID
    JOIN Movie ON Ticket.MovieID = Movie.MovieID;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("--- Booking Details ---")
        for row in results:
            print(f"Booking ID: {row[0]}, Ticket ID: {row[1]}, Cinema ID: {row[2]}, Movie Name: {row[3]}")
    else:
        print("No bookings found.")

    cursor.close()
    db.close()

def delete_entry(booking_id):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Booking WHERE BookingID = %s", (booking_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM Booking WHERE BookingID = %s", (booking_id,))
        print(f"Booking {booking_id} deleted successfully.")
    else:
        print(f"Booking {booking_id} not found.")

    db.commit()
    cursor.close()
    db.close()
def show_movies():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT MovieID, MovieName, MovieGenre, MovieLength FROM Movie")
    movies = cursor.fetchall()

    if movies:
        print("--- Movie List ---")
        for movie in movies:
            print(f"ID: {movie[0]}, Name: {movie[1]}, Genre: {movie[2]}, Length: {movie[3]} min")
    else:
        print("No movies found.")

    cursor.close()
    db.close()

def delete_movie():
    db = connect_db()
    cursor = db.cursor()

    MovieID = input("Enter Movie ID to delete: ")
    cursor.execute("SELECT * FROM Movie WHERE MovieID = %s", (MovieID,))

    if cursor.fetchone():
        cursor.execute("DELETE FROM Movie WHERE MovieID = %s", (MovieID,))
        db.commit()
        print(f"Movie {MovieID} deleted successfully.")
    else:
        print(f"Movie {MovieID} not found.")

    cursor.close()
    db.close()

def select_with_join():
    db = connect_db()
    cursor = db.cursor()

    query = """
    SELECT Booking.BookingID, Ticket.TicketID, Cinema.CinemaID, Movie.MovieName
    FROM Booking
    JOIN Ticket ON Booking.TicketID = Ticket.TicketID
    JOIN Cinema ON Ticket.CinemaID = Cinema.CinemaID
    JOIN Movie ON Ticket.MovieID = Movie.MovieID;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("--- Booking Details ---")
        for row in results:
            print(f"Booking ID: {row[0]}, Ticket ID: {row[1]}, Cinema ID: {row[2]}, Movie Name: {row[3]}")
    else:
        print("No bookings found.")

    cursor.close()
    db.close()



if __name__ == "__main__":
    while True:
        print("\n--- Movie Booking System ---")
        print("1. Insert a New Movie")
        print("2. Insert a New Customer")
        print("3. Show Movies")
        print("4. Show Bookings")
        print("5. Delete Booking")
        print("6. Delete Movie")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            insert_movie()
        elif choice == "2":
            insert_customer()
        elif choice == "3":
            show_movies()
        elif choice == "4":
            select_with_join()
        elif choice == "5":
            booking_id = int(input("Enter Booking ID to delete: "))
            delete_entry(booking_id)
        elif choice == "6":
            delete_movie()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")