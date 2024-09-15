# Ticket_Booking_System

The Ticket Booking System is a desktop application developed to simplify and manage ticket bookings using a user-friendly interface. The system is designed to handle various operations such as creating, updating, deleting, searching, and displaying all bookings efficiently. The application leverages MySQL for database management and Tkinter for the graphical user interface.

Key Features
1. Database Management:
Automatic Database Creation: The application checks for the existence of the required database and creates it if it does not exist. This includes setting up the necessary tables with fields like customer name, ticket type, event date, seat number, price, and ticket status to store booking information.

CRUD Operations: Users can perform Create, Read, Update, Delete, and even bulk delete operations on the bookings.

Data Integrity: Ensures data integrity and consistency through structured database queries and error handling mechanisms.

2. User Interface:
Tkinter Integration: The application uses Tkinter, Python’s standard GUI toolkit, to create an intuitive interface.

Input Fields and Buttons: The interface includes labeled input fields for booking ID, customer name, ticket type, event date, seat number, price, and ticket status. Buttons are available for creating, updating, deleting, searching bookings, displaying all bookings, and deleting all bookings.

3. Real-time Interaction:
Instant Feedback: Users receive immediate feedback on their actions, such as successful creation, deletion, and updating of bookings. Errors such as "Booking not found" are also handled and displayed.

Data Display: The application displays individual booking details after searching, as well as listing all bookings in the system neatly in the console.

Technical Details:
Programming Language: Python 3.x
Database: MySQL
Libraries and Tools:
mysql-connector-python: Used for connecting and interacting with the MySQL database.
tkinter: Used for creating the graphical user interface.
Visual Studio Code: Recommended development environment for writing and managing the application code.
How It Works:
1. Database Initialization:
Upon launching the application, it checks if the ticket_booking_system database exists. If not, it creates the database and the bookings table with the following fields:

booking_id: Unique ID for the booking (auto-increment).   
customer_name: Name of the customer.   
ticket_type: Type of the ticket (e.g., 3A, 2A).    
event_date: Date of the event.       
seat_number: The seat number assigned to the ticket.    
price: Price of the ticket.    
ticket_status: Status of the ticket (e.g., Confirmed, Cancelled).   

2. User Interaction:
Creating Bookings: Users enter details like customer name, ticket type, event date, seat number, price, and ticket status, then click the "Create" button to add a new booking.

Updating Bookings: Users can update existing booking details by entering the booking ID and modifying any of the available fields, such as customer name, ticket type, event date, seat number, price, and ticket status.

Deleting Bookings: Users can delete a specific booking by entering the booking ID and clicking the "Delete" button.

Searching Bookings: Users can search for a booking by entering the booking ID and clicking the "Search" button to retrieve and display the booking details.

Display All Bookings: Users can view all bookings stored in the database by clicking the "Display All" button, which neatly lists all the current bookings with their details.

Deleting All Bookings: Users can clear all bookings from the database by clicking the "Delete All" button to remove all data from the bookings table.

Project Aim:
This project aims to provide a comprehensive yet straightforward solution for managing ticket bookings, making it suitable for small to medium-sized event management needs. With its robust functionality, easy-to-use interface, and secure database handling, the Ticket Booking System ensures a smooth and efficient booking experience.
