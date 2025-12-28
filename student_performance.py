import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    total INTEGER,
    average REAL,
    grade TEXT
)
""")
conn.commit()


def add_student():
    name = input("Enter student name: ")

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    #SQL INSERT
    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (name, total, average, grade)
    )
    conn.commit()

    print("Student stored in database successfully!")
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- All Students ---")
    for row in records:
        print("Name:", row[0], "| Total:", row[1], "| Average:", row[2], "| Grade:", row[3])
def clear_students():
    cursor.execute("DELETE FROM students")
    conn.commit()
    print("All student records cleared.")

while True:
    print("\n--- Student Performance System ---")
    print("1. Add Student")
    print("2.view Students")
    print("3. Clear All Records")
    print("4. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        clear_students()
    elif choice == "4":
        print("Exiting program...")
        break

conn.close()
