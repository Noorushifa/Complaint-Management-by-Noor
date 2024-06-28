## Hi there 👋
This is NOORUSHIFA.

<
PROJECT: Complaint Management System 
LEVEL: Basic level

This code is a well-structured example of a Complaint Management System using Python's Tkinter library and SQLite3 for data storage. Here's a breakdown of the functionality:

Database Management:
It uses the sqlite3 library to connect to a database file named "informationDB.db".
The ConnectionDatabase class handles database interactions:
Creates a table named "complainTable" if it doesn't exist, with columns for ID (auto-incrementing primary key), Name, Mobile No, Address, Role, and Comment.

Provides methods to:
Add new complaints to the database (Add function).
Retrieve a list of existing complaints (ListRequest function).

User Interface:
It utilizes the tkinter library to create a graphical user interface (GUI) window.

The GUI allows users to:
Enter their name, mobile number, address, role (employee or user), and complaint details in a text box.
Submit the complaint by clicking the "Submit Now" button.
View a list of existing complaints by clicking the "View Complain" button (which opens a separate window).

Workflow:

User enters complaint information in the GUI.
Clicking "Submit Now" triggers the SaveData function.
SaveData retrieves data from entry fields and the text box.
It calls the ConnectionDatabase.Add method to add the complaint to the database.
The function clears the entry fields, displays a success message, and resets the comment text box.
Clicking "View Complain" creates an instance of the ComplaintListing class.
ComplaintListing retrieves a list of complaints from the database using ConnectionDatabase.ListRequest.
It populates a Tkinter Treeview widget with the complaint details (ID, Name, Mobile No, Address, Role, Comment) in a separate window.

Overall, this code provides a basic framework for a complaint management system.

Thanks and regards,
Noorushifa.

-->
