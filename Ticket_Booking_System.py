import tkinter as tk
import mysql.connector

# Function to check if the database exists and create it if it doesn't
def check_database():
    # Create a temporary connection without specifying the database name
    temp_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password
    )
    temp_cursor = temp_db.cursor()

    # Check if the database exists
    temp_cursor.execute("SHOW DATABASES")
    databases = temp_cursor.fetchall()
    database_exists = False

    for database in databases:
        if "ticket_booking_system" in database:
            database_exists = True
            break

    if database_exists:
        # If the database exists, check if the columns exist in the table
        temp_cursor.execute("USE ticket_booking_system")
        temp_cursor.execute("SHOW COLUMNS FROM bookings")
        columns = temp_cursor.fetchall()
        column_names = [column[0] for column in columns]

        # Check and add missing columns
        if "event_date" not in column_names:
            temp_cursor.execute("ALTER TABLE bookings ADD event_date DATE")
        if "seat_number" not in column_names:
            temp_cursor.execute("ALTER TABLE bookings ADD seat_number VARCHAR(10)")
        if "price" not in column_names:
            temp_cursor.execute("ALTER TABLE bookings ADD price DECIMAL(10, 2)")
        if "ticket_status" not in column_names:
            temp_cursor.execute("ALTER TABLE bookings ADD ticket_status VARCHAR(50)")

        print("Table updated with missing columns!")

    else:
        # Create the database and table if it doesn't exist
        temp_cursor.execute("CREATE DATABASE ticket_booking_system")
        temp_db.commit()

        temp_cursor.execute("USE ticket_booking_system")
        temp_cursor.execute("""
        CREATE TABLE bookings (
            booking_id INT AUTO_INCREMENT PRIMARY KEY, 
            customer_name VARCHAR(255), 
            ticket_type VARCHAR(255), 
            event_date DATE, 
            seat_number VARCHAR(10), 
            price DECIMAL(10, 2), 
            ticket_status VARCHAR(50)
        )""")
        temp_db.commit()

        print("Database and table created successfully!")

    temp_cursor.close()
    temp_db.close()

# Function to create a new booking
def create_booking():
    customer_name = entry_customer_name.get()
    ticket_type = entry_ticket_type.get()
    event_date = entry_event_date.get()
    seat_number = entry_seat_number.get()
    price = entry_price.get()
    ticket_status = entry_ticket_status.get()

    # Insert the booking into the database
    query = "INSERT INTO bookings (customer_name, ticket_type, event_date, seat_number, price, ticket_status) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (customer_name, ticket_type, event_date, seat_number, price, ticket_status)
    cursor.execute(query, values)
    db.commit()

    # Clear the entry fields
    entry_customer_name.delete(0, tk.END)
    entry_ticket_type.delete(0, tk.END)
    entry_event_date.delete(0, tk.END)
    entry_seat_number.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_ticket_status.delete(0, tk.END)

    print("Booking created successfully!")

# Function to delete a booking
def delete_booking():
    booking_id = entry_booking_id.get()

    # Delete the booking from the database
    query = "DELETE FROM bookings WHERE booking_id = %s"
    values = (booking_id,)
    cursor.execute(query, values)
    db.commit()

    # Clear the entry field
    entry_booking_id.delete(0, tk.END)

    print("Booking deleted successfully!")

# Function to update a booking
def update_booking():
    booking_id = entry_booking_id.get()
    customer_name = entry_customer_name.get()
    ticket_type = entry_ticket_type.get()
    event_date = entry_event_date.get()
    seat_number = entry_seat_number.get()
    price = entry_price.get()
    ticket_status = entry_ticket_status.get()

    # Update the booking in the database
    query = "UPDATE bookings SET customer_name = %s, ticket_type = %s, event_date = %s, seat_number = %s, price = %s, ticket_status = %s WHERE booking_id = %s"
    values = (customer_name, ticket_type, event_date, seat_number, price, ticket_status, booking_id)
    cursor.execute(query, values)
    db.commit()

    # Clear the entry fields
    entry_booking_id.delete(0, tk.END)
    entry_customer_name.delete(0, tk.END)
    entry_ticket_type.delete(0, tk.END)
    entry_event_date.delete(0, tk.END)
    entry_seat_number.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_ticket_status.delete(0, tk.END)

    print("Booking updated successfully!")

# Function to search for a booking and display it neatly
def search_booking():
    booking_id = entry_booking_id.get()

    # Search for the booking in the database
    query = "SELECT * FROM bookings WHERE booking_id = %s"
    values = (booking_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        print("\n" + "-" * 40)
        print(f"Booking ID: {result[0]}")
        print(f"Customer Name: {result[1]}")
        print(f"Ticket Type: {result[2]}")
        print(f"Event Date: {result[3]}")
        print(f"Seat Number: {result[4]}")
        print(f"Price: {result[5]}")
        print(f"Ticket Status: {result[6]}")
        print("-" * 40 + "\n")
    else:
        print("Booking not found!")

# Function to display all bookings neatly
def display_all_bookings():
    query = "SELECT * FROM bookings"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("\n" + "=" * 60)
        for row in results:
            print(f"Booking ID: {row[0]}")
            print(f"Customer Name: {row[1]}")
            print(f"Ticket Type: {row[2]}")
            print(f"Event Date: {row[3]}")
            print(f"Seat Number: {row[4]}")
            print(f"Price: {row[5]}")
            print(f"Ticket Status: {row[6]}")
            print("-" * 60)
        print("=" * 60 + "\n")
    else:
        print("No bookings found!")

# Function to delete all bookings
def delete_all_bookings():
    query = "DELETE FROM bookings"
    cursor.execute(query)
    db.commit()
    print("All bookings deleted successfully!")

# Ask the user to input the database password
db_password = input("Enter the database password: ")

# Check if the database exists and create it if necessary
check_database()

# Create a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="ticket_booking_system"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create the Tkinter application window
window = tk.Tk()
window.title("Ticket Booking System")

# Create labels
label_booking_id = tk.Label(window, text="Booking ID:")
label_booking_id.grid(row=0, column=0)

label_customer_name = tk.Label(window, text="Customer Name:")
label_customer_name.grid(row=1, column=0)

label_ticket_type = tk.Label(window, text="Ticket Type:")
label_ticket_type.grid(row=2, column=0)

label_event_date = tk.Label(window, text="Event Date (YYYY-MM-DD):")
label_event_date.grid(row=3, column=0)

label_seat_number = tk.Label(window, text="Seat Number:")
label_seat_number.grid(row=4, column=0)

label_price = tk.Label(window, text="Price:")
label_price.grid(row=5, column=0)

label_ticket_status = tk.Label(window, text="Ticket Status:")
label_ticket_status.grid(row=6, column=0)

# Create entry fields
entry_booking_id = tk.Entry(window)
entry_booking_id.grid(row=0, column=1)

entry_customer_name = tk.Entry(window)
entry_customer_name.grid(row=1, column=1)

entry_ticket_type = tk.Entry(window)
entry_ticket_type.grid(row=2, column=1)

entry_event_date = tk.Entry(window)
entry_event_date.grid(row=3, column=1)

entry_seat_number = tk.Entry(window)
entry_seat_number.grid(row=4, column=1)

entry_price = tk.Entry(window)
entry_price.grid(row=5, column=1)

entry_ticket_status = tk.Entry(window)
entry_ticket_status.grid(row=6, column=1)

# Create buttons
btn_create = tk.Button(window, text="Create", command=create_booking)
btn_create.grid(row=7, column=0)

btn_delete = tk.Button(window, text="Delete", command=delete_booking)
btn_delete.grid(row=7, column=1)

btn_update = tk.Button(window, text="Update", command=update_booking)
btn_update.grid(row=8, column=0)

btn_search = tk.Button(window, text="Search", command=search_booking)
btn_search.grid(row=8, column=1)

btn_display_all = tk.Button(window, text="Display All", command=display_all_bookings)
btn_display_all.grid(row=9, column=0)

btn_delete_all = tk.Button(window, text="Delete All", command=delete_all_bookings)
btn_delete_all.grid(row=9, column=1)

# Run the Tkinter main loop
window.mainloop()

# Close the cursor and database connection when done
cursor.close()
db.close()

