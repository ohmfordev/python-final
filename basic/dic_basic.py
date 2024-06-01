# Dictionary operations
my_dict = {"name": "Ohm",
            "age": 25, 
            "city": "BKK"}
print("Original dictionary:", my_dict)

# Adding key-value pairs
my_dict["email"] = "alice@example.com"
print("After adding email:", my_dict)


# Updating values
my_dict["age"] = 26
print("After updating age:", my_dict)

# Removing key-value pairs
del my_dict["city"]
print("After deleting city:", my_dict)

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))

# Iterating through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")



    # Array (List) of dictionaries
people = [
    {"name": "Ohm", "age": 25, "city": "BKK"},
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 22, "city": "SF"}
]

# Accessing elements in the array of dictionaries
for person in people:
    print(person)


people[0]["name"] = 80
print("Updated people:", people)


people[0] = {"name": "Nut", "age": 36}
print("Updated people:", people)