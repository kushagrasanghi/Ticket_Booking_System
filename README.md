# Ticket_Booking_System

The Ticket Booking System is a desktop application developed to simplify and manage ticket bookings using a user-friendly interface. The system is designed to handle various operations such as creating, updating, deleting, and searching bookings efficiently. The application leverages the power of MySQL for database management and Tkinter for the graphical user interface.

Key Features
1) Database Management:
   
  Automatic Database Creation: The application checks for the existence of the required database and creates it if it does not exist. This includes setting up the necessary tables to store booking information.
  CRUD Operations: Users can perform Create, Read, Update, and Delete operations on the bookings.
  Data Integrity: Ensures data integrity and consistency through structured database queries and error handling.
  
2) User Interface:
   
  Tkinter Integration: The application uses Tkinter, a standard Python interface to the Tk GUI toolkit, to create a simple and intuitive interface.
  Input Fields and Buttons: The interface includes labeled input fields for booking ID, customer name, and ticket type, along with buttons for creating, updating, deleting, and searching bookings. 
  
3)Real-time Interaction: 

  Instant Feedback: Users receive immediate feedback on their actions, such as successful creation, deletion, and updating of bookings, or errors like booking not found. 
  Data Display: The application displays the booking details retrieved from the database, providing users with clear and concise information. 
  
Technical Details 
  Programming Language: Python 3 
  
  Database: MySQL 
  
  Libraries and Tools: 
    -mysql.connector: Used for connecting and interacting with the MySQL database. 
    -tkinter: Used for creating the graphical user interface. 
    -Visual Studio Code: Recommended development environment for writing and managing the application code. 
    
How It Works 

1) Database Initialization: Upon launching the application, it checks if the ticket_booking_system database exists. If not, it creates the database and the bookings table.
2) User Interaction: 
  Creating Bookings: Users enter the booking ID, customer name, and ticket type, and click the "Create" button to add a new booking.
  Updating Bookings: Users can update existing booking details by entering the booking ID and the new information. 
  Deleting Bookings: Users can delete a booking by entering the booking ID and clicking the "Delete" button. 
  Searching Bookings: Users can search for a booking by entering the booking ID and clicking the "Search" button to retrieve and display the booking details. 

This project aims to provide a straightforward and efficient solution for managing ticket bookings, making it an ideal choice for small to medium-sized event management needs. With its robust functionality and user-friendly design, the Ticket Booking System ensures a smooth and hassle-free booking experience. 
