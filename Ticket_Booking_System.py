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

    # Create the database and table if it doesn't exist
    if not database_exists:
        temp_cursor.execute("CREATE DATABASE ticket_booking_system")
        temp_db.commit()

        temp_cursor.execute("USE ticket_booking_system")
        temp_cursor.execute("CREATE TABLE bookings (booking_id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255), ticket_type VARCHAR(255))")
        temp_db.commit()

        print("Database and table created successfully!")

    temp_cursor.close()
    temp_db.close()

# Function to create a new booking
def create_booking():
    booking_id = entry_booking_id.get()
    customer_name = entry_customer_name.get()
    ticket_type = entry_ticket_type.get()

    # Insert the booking into the database
    query = "INSERT INTO bookings (booking_id, customer_name, ticket_type) VALUES (%s, %s, %s)"
    values = (booking_id, customer_name, ticket_type)
    cursor.execute(query, values)
    db.commit()

    # Clear the entry fields
    entry_booking_id.delete(0, tk.END)
    entry_customer_name.delete(0, tk.END)
    entry_ticket_type.delete(0, tk.END)

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

    # Update the booking in the database
    query = "UPDATE bookings SET customer_name = %s, ticket_type = %s WHERE booking_id = %s"
    values = (customer_name, ticket_type, booking_id)
    cursor.execute(query, values)
    db.commit()

    # Clear the entry fields
    entry_booking_id.delete(0, tk.END)
    entry_customer_name.delete(0, tk.END)
    entry_ticket_type.delete(0, tk.END)

    print("Booking updated successfully!")

# Function to search for a booking
def search_booking():
    booking_id = entry_booking_id.get()

    # Search for the booking in the database
    query = "SELECT * FROM bookings WHERE booking_id = %s"
    values = (booking_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        # Display the booking details
        customer_name = result[1]
        ticket_type = result[2]
        print(f"Booking ID: {booking_id}\nCustomer Name: {customer_name}\nTicket Type: {ticket_type}")
    else:
        print("Booking not found!")

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

# Create entry fields
entry_booking_id = tk.Entry(window)
entry_booking_id.grid(row=0, column=1)

entry_customer_name = tk.Entry(window)
entry_customer_name.grid(row=1, column=1)

entry_ticket_type = tk.Entry(window)
entry_ticket_type.grid(row=2, column=1)

# Create buttons
btn_create = tk.Button(window, text="Create", command=create_booking)
btn_create.grid(row=3, column=0)

btn_delete = tk.Button(window, text="Delete", command=delete_booking)
btn_delete.grid(row=3, column=1)

btn_update = tk.Button(window, text="Update", command=update_booking)
btn_update.grid(row=4, column=0)

btn_search = tk.Button(window, text="Search", command=search_booking)
btn_search.grid(row=4, column=1)

# Start the Tkinter event loop
window.mainloop()
