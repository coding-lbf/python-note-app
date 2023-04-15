# Create a Note App with Python

# Import necessary modules
import os
import sys

# Define the main function
def main():
    # Print welcome message
    print("Welcome to the Note App!")
    
    # Ask user for input
    user_input = input("What would you like to do? (Create, Read, Update, Delete): ")
    
    # Check user input
    if user_input == "Create":
        create_note()
    elif user_input == "Read":
        read_note()
    elif user_input == "Update":
        update_note()
    elif user_input == "Delete":
        delete_note()
    else:
        print("Invalid input. Please try again.")
        main()
        
# Define the create_note function
def create_note():
    # Ask user for note title
    note_title = input("Please enter a title for your note: ")
    
    # Ask user for note content
    note_content = input("Please enter the content of your note: ")
    
    # Create the note file
    note_file = open(note_title + ".txt", "w")
    
    # Write the note content to the file
    note_file.write(note_content)
    
    # Close the file
    note_file.close()
    
    # Print success message
    print("Note created successfully!")
    
    # Return to main menu
    main()
    
# Define the read_note function
def read_note():
    # Ask user for note title
    note_title = input("Please enter the title of the note you want to read: ")
    
    # Open the note file
    note_file = open(note_title + ".txt", "r")
    
    # Read the note content
    note_content = note_file.read()
    
    # Print the note content
    print(note_content)
    
    # Close the file
    note_file.close()
    
    # Return to main menu
    main()
    
# Define the update_note function
def update_note():
    # Ask user for note title
    note_title = input("Please enter the title of the note you want to update: ")
    
    # Open the note file
    note_file = open(note_title + ".txt", "a")
    
    # Ask user for new note content
    new_note_content = input("Please enter the new content of your note: ")
    
    # Append the new note content to the file
    note_file.write(new_note_content)
    
    # Close the file
    note_file.close()
    
    # Print success message
    print("Note updated successfully!")
    
    # Return to main menu
    main()
    
# Define the delete_note function
def delete_note():
    # Ask user for note title
    note_title = input("Please enter the title of the note you want to delete: ")
    
    # Delete the note file
    os.remove(note_title + ".txt")
    
    # Print success message
    print("Note deleted successfully!")
    
    # Return to main menu
    main()
    
# Call the main function
if __name__ == "__main__":
    main()
