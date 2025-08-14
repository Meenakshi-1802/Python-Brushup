# Multiple Variable Initialization 

## 1. What is Multiple Initialization?

Multiple initialization means assigning the same value or different values to multiple variables in a single line instead of writing multiple separate assignment statements.

## 2. Assigning the Same Value to Multiple Variables

We can assign the same value to multiple variables at once like this:

a = b = 7
print(a, b)   # Output: 7 7


## How it works:

## Python evaluates the value (7) first.

## Then assigns the reference of that value to both variables a and b.

## Now, both a and b point to the same object in memory (important for mutable objects).
