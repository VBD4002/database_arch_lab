import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# Create a table for notes if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')
conn.commit()

# Function to add a note
def add_note(title, content):
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    print("Note added successfully!")

# Function to view all notes
def view_notes():
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}")

# Function to delete a note by ID
def delete_note(note_id):
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    print(f"Note with ID {note_id} deleted successfully!")

# Main program loop
while True:
    print("\n--- Note-Taking App ---")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Delete a Note")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == '2':
        view_notes()
    elif choice == '3':
        note_id = input("Enter the ID of the note to delete: ")
        delete_note(note_id)
    elif choice == '4':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
