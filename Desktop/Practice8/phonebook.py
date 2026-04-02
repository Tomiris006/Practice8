from connect import connect

def call_search():
    conn = connect()
    cur = conn.cursor()

    word = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (word,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_upsert():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


def call_pagination():
    conn = connect()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_delete():
    conn = connect()
    cur = conn.cursor()

    value = input("Enter name or phone: ")
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()


def call_insert_many():
    conn = connect()
    cur = conn.cursor()

    names = ["Ali", "Dana", "Test"]
    phones = ["8700123", "12345", "8700555"]

    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    conn.commit()

    cur.close()
    conn.close()


def menu():
    while True:
        print("""
1 - Search
2 - Add/Update
3 - Pagination
4 - Delete
5 - Insert Many
6 - Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            call_search()
        elif choice == "2":
            call_upsert()
        elif choice == "3":
            call_pagination()
        elif choice == "4":
            call_delete()
        elif choice == "5":
            call_insert_many()
        elif choice == "6":
            break


menu()