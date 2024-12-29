# Python Data Structures Showcase

This repository showcases examples of **Lists**, **Dictionaries**,**Stets**, and **Tuples** in Python. These are some of the most commonly used data structures in Python, and understanding them is key to mastering the language.

## Table of Contents
- [Lists](#lists)
- [Dictionaries](#dictionaries)
- [Tuples](#tuples)
- [Sets] (#Sets)

---

## Lists

Lists are ordered collections that can hold items of different types. You can modify a list by adding, removing, or changing items.

### Example:
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Adding an item
fruits.append("orange")

# Removing an item
fruits.remove("banana")

# Accessing elements
print(fruits[0])  # Output: apple

# List slicing
print(fruits[1:3])  # Output: ['cherry', 'orange']
Dictionaries are unordered collections of key-value pairs. Each key must be unique, and you can access values via their keys.
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values by key
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Removing a key-value pair
del person["age"]

# Iterating over keys and values
for key, value in person.items():
    print(key, value)

