contact_book = {
    "Ravi": "9876543210",
    "Anita": "9123456780"
}

print("Contact List:")
for name, number in contact_book.items():
    print(f"{name}: {number}")

search_name = input("\nEnter a name to search: ")

if search_name in contact_book:
    print(f"Phone number of {search_name}: {contact_book[search_name]}")
else:
    print("Contact not found")