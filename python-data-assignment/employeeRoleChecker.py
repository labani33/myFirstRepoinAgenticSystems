employee = (101, "Rahul Sharma", "IT")
roles = {"admin", "editor", "viewer"}

print("Employee Details:")
print(f"ID: {employee[0]}")
print(f"Name: {employee[1]}")
print(f"Department: {employee[2]}")
if "admin" in roles:
    print("\nAdmin Access: Yes")
else:
    print("\nAdmin Access: No")