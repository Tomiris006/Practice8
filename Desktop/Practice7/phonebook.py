from connect import connect
import csv

# -------------------- CREATE TABLE --------------------
def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


# -------------------- INSERT FROM CSV --------------------
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV!")


# -------------------- SHOW ALL --------------------
def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# -------------------- INSERT FROM CONSOLE --------------------
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")


# -------------------- UPDATE --------------------
def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Updated!")


# -------------------- SEARCH --------------------
def search_contacts():
    keyword = input("Search name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s",
        ('%' + keyword + '%',)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# -------------------- DELETE --------------------
def delete_contact():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name = %s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted!")


# -------------------- MENU --------------------
def menu():
    create_table()  # создаем таблицу при запуске

    while True:
        print("\n1. Show all")
        print("2. Insert from CSV")
        print("3. Add contact")
        print("4. Update contact")
        print("5. Search")
        print("6. Delete")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_all()

        elif choice == "2":
            insert_from_csv()

        elif choice == "3":
            insert_from_console()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            search_contacts()

        elif choice == "6":
            delete_contact()

        elif choice == "7":
            break

        else:
            print("Invalid choice")


# -------------------- START --------------------
menu()