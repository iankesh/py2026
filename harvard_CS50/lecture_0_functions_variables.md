# CS50P — Lecture 0: Functions, Variables

- **Course:** Harvard CS50’s Introduction to Programming with Python
- **Instructor:** David J. Malan
- **Video:** [Watch Lecture 0 on YouTube](https://youtu.be/nLRL_NcnK-4?si=qANOfDsaaqo6DuOu)

---

## Key Concepts

### 1. Functions
- **Definition:** A reusable block of code or an action/verb in programming designed to carry out a specific task.
- **Built-in Functions:** Python provides ready-to-use functions like `print()`, `input()`, `int()`, `float()`, `round()`.
- **Calling / Invoking:** Executing a function by writing its name followed by parentheses: `function_name()`.
- **Custom Functions:** Defined using the `def` keyword.

### 2. Variables & Assignment (`variable = input()`)
- **What is a Variable?**
  - A variable is a named container or storage location in computer memory that holds a value so you can refer to, use, or modify it later in your program.
- **How Assignment Works: `variable = input(...)`**
  - The single equals sign `=` is the **assignment operator** (NOT algebraic equality; equality in Python is `==`).
  - **Right-to-Left Evaluation:**
    1. Python evaluates whatever is on the **right side** first:
       - Calls `input("What's your name? ")`.
       - Prompts the user and waits for them to type text and press Enter.
       - Returns the text as a string (e.g., `"Alice"`).
    2. Python then **copies/assigns** that value into the variable on the **left side** (`name`).
  - *Mental Model:*
    ```text
    name  <--- (stores) <---  input("What's your name? ")  ["Alice"]
    ```
- **Variable Reassignment (Updating Values):**
  - Variables can have their values updated or overwritten at any time:
    ```python
    name = input("Name: ")   # e.g., "  alice  "
    name = name.strip()      # Reassigns 'name' with whitespace removed: "alice"
    name = name.capitalize() # Reassigns 'name' capitalized: "Alice"
    ```
- **Python Variable Naming Conventions (PEP 8):**
  - Use `snake_case` (all lowercase words separated by underscores): `user_name`, `first_name`, `total_score`.
  - Must start with a letter (a-z, A-Z) or an underscore `_`, **never a number** (e.g., `1name` is invalid; `name1` is valid).
  - Can only contain alphanumeric characters and underscores (`a-z`, `0-9`, `_`).
  - **Case-sensitive:** `name`, `Name`, and `NAME` are three completely different variables.
  - Choose clear, descriptive names instead of vague single letters (e.g., use `student_name` instead of `s`).

### 3. Arguments (vs. Parameters)
- **Argument:** The actual input or value passed into a function inside the parentheses when you *call* it.
  - *Example:* In `print("hello, world")`, `"hello, world"` is an argument.
- **Parameter:** The placeholder variable defined in the function signature that receives the argument.
- **Types of Arguments:**
  - **Positional Arguments:** Matched by position/order (e.g., `print("Hello,", name)`).
  - **Named / Keyword Arguments:** Passed by name with optional default values (e.g., `print("Hello", end="???")`, `sep=" "`).

### 4. Side Effects (vs. Return Values)
- **Side Effect:** Any observable effect or action a function performs outside its own scope besides returning a value.
  - *Example:* Displaying text onto the screen/terminal using `print()` is a **side effect**.
  - Writing data to a file, playing a sound, or modifying a global state are also side effects.
- **Return Value:** The actual output or data that a function hands back to the program using the `return` keyword.
  - *Example:* `input("What's your name? ")` returns a string value you can store in a variable.
  - *Important distinction:* `print()` produces a side effect (prints to the console), but its return value is `None`.

### 5. Getting User Input (`input()`)
- **The `input()` Function:** Prompts the user with an optional message, pauses execution, and waits for the user to type text and press **Enter**.
- **Always Returns a String (`str`):** Regardless of what the user types (even digits like `50`), `input()` *always* returns it as a string (`"50"`).
- **Cleaning & Formatting Input (String Methods):**
  - `.strip()`: Removes leading and trailing whitespace from the string.
  - `.capitalize()`: Capitalizes only the very first character of the string.
  - `.title()`: Capitalizes the first letter of *each word* (e.g., `"david malan"` -> `"David Malan"`).
  - **Method Chaining:** Calling multiple methods sequentially in a single line, e.g., `input("Name: ").strip().title()`.
  - `.split()`: Splits a string into a list or multiple variables based on a separator (e.g., `first, last = name.split(" ")`).
- **Type Conversion (Casting):**
  - If you need numerical calculations, you must explicitly convert the returned string using `int()` (integer) or `float()` (decimal number):
    - `x = int(input("What's x? "))`

### 6. The `return` Keyword
- **Definition:** A statement used inside a function to send a result/value back to the caller (where the function was invoked).
- **Immediate Termination:** As soon as Python encounters a `return` statement, the function terminates instantly. Any lines of code directly below it in that function are skipped.
- **Why use `return` instead of `print()`?**
  - **Reusability & Composability:** When a function returns a value, that value can be:
    - Stored in a variable: `result = square(5)`
    - Used directly in arithmetic: `total = square(3) + square(4)`
    - Passed into another function: `print(square(5))`
    - Verified in automated tests (unit tests).
  - **Separation of Concerns:** A function should do one job well (e.g., compute a square) rather than forcing output to the screen. The caller gets to decide how to use the result.
- **Implicit Return (`None`):** If a function executes to its end without hitting an explicit `return`, Python automatically returns `None`.
- **Early Return (Guard Clauses):** You can use `return` inside conditionals to exit early from a function if certain invalid conditions or edge cases are met.
- **Returning Multiple Values:** A function can return multiple values separated by commas (packed as a tuple): `return x, y`.

---

## Code Examples & Patterns

```python
# 1. Variable Assignment with input()
# Step 1: Right side runs first -> input(...) prompts user and returns a string
# Step 2: The '=' operator assigns that value into the variable 'name' on the left
name = input("What's your name? ")
print(f"hello, {name}")

# Variable Reassignment (updating the variable's stored value)
name = name.strip().title()
print(f"hello cleaned name, {name}")

# 2. Cleaning User Input with String Methods
# Removing whitespace and capitalizing each word
raw_name = input("What's your full name? ")
clean_name = raw_name.strip().title()
print(f"hello, {clean_name}")

# 3. Method Chaining (Clean and concise in one line)
name = input("What's your name? ").strip().title()
print(f"hello, {name}")

# 4. Splitting User Input into Multiple Variables
full_name = input("Enter first and last name: ").strip().title()
first, last = full_name.split(" ")
print(f"First name: {first}, Last name: {last}")

# 5. Numeric Input & Type Casting (int and float)
# Without int(), "1" + "2" results in "12" (string concatenation)
x = int(input("What's x? "))
y = int(input("What's y? "))
print("Sum:", x + y)

# Decimal numbers with float() and rounding
a = float(input("What's a? "))
b = float(input("What's b? "))
z = round(a + b, 2)
print(f"Formatted sum: {z:,}")  # Format with commas for thousands

# 6. Function with 'return' (Reusable & Composable)
def square(n):
    return n * n

# Returned value can be stored in a variable:
squared_val = square(4)  # 16

# Returned value can be composed in expressions or print():
print("Square of 4 is:", square(4))
print("Hypotenuse squared (3^2 + 4^2):", square(3) + square(4))  # 9 + 16 = 25

# 7. Immediate Termination with 'return'
def check_number(n):
    if n < 0:
        return "Negative number"
    return "Positive or Zero"
    print("This line will NEVER run because return already exited!")

# 8. Returning Multiple Values
def get_dimensions():
    width = 1920
    height = 1080
    return width, height  # Returns a tuple

w, h = get_dimensions()
print(f"Width: {w}, Height: {h}")
```

---

## Tips & Common Pitfalls

- **Confusing `print()` with `return`:**
  - `print()` displays text on the screen for the human eye (a side effect). You cannot save, pass, or compute with it.
  - `return` sends data back into your code so other parts of the program can use it.
- **Accidentally relying on a function that doesn't return:**
  - If a function doesn't have `return`, its return value is `None`. Doing `result = greet("Alice")` will make `result == None`.
- **Code after `return` is unreachable:**
  - Any statement following `return` inside the same execution block will never execute.
- **Input is always a string (`str`):**
  - If you write `x = input("x: ")` and `y = input("y: ")`, doing `x + y` concatenates the strings (e.g., `"2"` + `"3"` = `"23"`). Always wrap with `int()` or `float()` if you intend to do arithmetic.
- **`split()` errors with unexpected input:**
  - `first, last = name.split(" ")` will raise a `ValueError` if the user enters only one word or more than two words.
- **Default Arguments:** Always place positional parameters before parameters with default values when defining functions (`def hello(to="world")`).
