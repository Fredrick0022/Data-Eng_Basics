#!/bin/bash
chmod +x ctd_statment.sh
# Print a message
echo "Hello, World!"

# Variables
name="John"
echo "Hello, $name!"

# Conditional statements
if [ "$name" = "John" ]; then
  echo "Welcome, John!"
else
  echo "I don't recognize you."
fi

# Loops
for i in {1..5}; do
  echo "Count: $i"
done

# Functions
greet() {
  echo "Hello, $1!"
}
greet "Alice"

# Reading input
echo "What's your favorite color?"
read color
echo "Your favorite color is $color."
 
