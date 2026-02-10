age=int(input("Please enter your age: "))
has_ID = input("Has ID? (True/False): ").strip().lower() == "true"
if(age>=18 and has_ID):
    print("Entry allowed")
    print(type(has_ID))
else:
    print("Entry Denied")