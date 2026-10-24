# CS50P — Lecture 2: Loops

- **Course:** Harvard CS50’s Introduction to Programming with Python
- **Instructor:** David J. Malan
- **Video:** [Watch Lecture 2 on YouTube](https://youtu.be/nLRL_NcnK-4?si=qANOfDsaaqo6DuOu)

---

## Key Concepts

### 1. What are Loops?
- **Definition:** Control structures that repeat a block of code multiple times.
- **The Core Problem They Solve:** Eliminates copying and pasting identical code (violating the **DRY — Don't Repeat Yourself** principle).

---

### 2. The Naive Approach: Copy-Pasting (`cat.py`)

David Malan starts by asking: *"How do we make a cat meow 3 times?"*

```python
# The Bad Way: Copy-Paste
print("meow")
print("meow")
print("meow")
```
- **Why this fails in real programming:**
  - What if the cat needs to meow 500 times? Or 1,000,000 times?
  - Changing `"meow"` to `"woof"` requires editing every single line.

---

### 3. The `while` Loop

A **`while` loop** repeats a block of code **as long as a Boolean condition remains `True`**.

#### A. Syntax & Three Mandatory Ingredients:
Every standard counting `while` loop requires 3 distinct parts:
1. **Initialization:** Set a counter variable *before* the loop starts (`i = 0` or `i = 3`).
2. **Condition:** A test evaluated before every iteration (`while i < 3:`).
3. **Update / Increment:** Modify the counter inside the loop body so it eventually terminates (`i += 1`).

```python
i = 0          # 1. Initialize counter
while i < 3:   # 2. Check condition
    print("meow")
    i += 1     # 3. Increment counter
```

#### B. Step-by-Step Execution Trace:
| Iteration | Value of `i` | Condition `i < 3` | Action Taken | Next `i` (`i += 1`) |
| :---: | :---: | :---: | :--- | :---: |
| **Start** | `0` | `0 < 3` &rarr; `True` | Prints `"meow"` | `0 + 1 = 1` |
| **2nd** | `1` | `1 < 3` &rarr; `True` | Prints `"meow"` | `1 + 1 = 2` |
| **3rd** | `2` | `2 < 3` &rarr; `True` | Prints `"meow"` | `2 + 1 = 3` |
| **End** | `3` | `3 < 3` &rarr; **`False`** | **Loop terminates immediately!** | Exit |

---

### 4. Counting Up vs. Counting Down

#### Counting Up (Convention in Computer Science):
Computer scientists typically count from `0` up to `n - 1`:
```python
i = 0
while i < 3:
    print("meow")
    i += 1  # Runs for i = 0, 1, 2
```

#### Counting Down:
You can also count backwards towards `0`:
```python
i = 3
while i > 0:
    print("meow")
    i -= 1  # Runs for i = 3, 2, 1
```

---

### 5. Assignment Operators & The Absence of `++` / `--`

#### A. Compound Assignment Operators
Python provides shorthand operators to update variables in place:
- **`i += 1`** &rarr; Equivalent to `i = i + 1` (Increment by 1)
- **`i -= 1`** &rarr; Equivalent to `i = i - 1` (Decrement by 1)
- **`i *= 2`** &rarr; Equivalent to `i = i * 2` (Multiply in place)
- **`i /= 2`** &rarr; Equivalent to `i = i / 2` (Divide in place)

#### B. Why Python Does NOT Have `i++`, `i--`, `++i`, or `--i`
Coming from languages like C, C++, Java, or JavaScript, beginners often try to use `i++` or `i--`. **Python deliberately omitted them by design.**

1. **`i++` and `i--` cause a `SyntaxError`:**
   ```python
   i = 0
   i++  # 💥 SyntaxError: invalid syntax
   ```
   - *Why?* Python's core design philosophy (The Zen of Python) values **simplicity and readability**. `i++` mixes an expression and a state modification on one line, which Python avoids.

2. **The Sneaky Gotcha with `++i` and `--i` (No Error, But Doesn't Increment!):**
   If you accidentally type `++i` in Python, **it will not crash, but it will NOT increment either**:
   ```python
   i = 5
   ++i
   print(i)  # Still outputs: 5 !
   ```
   - *Why?* Python interprets `+` as the **unary positive operator** (like `+5` being positive five).
   - So `++i` is just parsed as `+(+(i))`, which simply evaluates to `5` and does nothing!
   - Similarly, `--i` is parsed as `-(-(i))`, which cancels two negatives and still evaluates to `5` without changing `i`.

- **The Universal Rule:** Always use **`i += 1`** or **`i -= 1`** in Python.

---

### 6. The Danger: Infinite Loops

If your condition never becomes `False`, Python runs forever in an **infinite loop**:

```python
# ❌ BUG: Forgot to increment 'i'!
i = 0
while i < 3:
    print("meow")
    # 'i' stays 0 forever -> 0 is always < 3!
```
- **How to stop an infinite loop in terminal:** Press **`Ctrl + C`** (sends a `KeyboardInterrupt` signal).

---

### 7. New Data Type: `list`

Before introducing `for` loops, David Malan introduces a major new built-in data type: the **`list`**.

#### A. What is a `list`?
- **Square Brackets `[ ]` Define a List:** In Python code, square brackets denote a list literal.
- **Definition:** An ordered, mutable (changeable) sequence of values enclosed in **`[ ]`**, separated by commas.
- While a primitive variable (`int`, `float`, `str`) holds a single value, a `list` can hold **multiple values** in a single container.

```python
# A list of numbers
numbers = [0, 1, 2]

# A list of strings
students = ["Hermione", "Harry", "Ron"]

# An empty list
empty = []
```

#### B. The Two Roles of Square Brackets `[ ]` with Lists:
1. **Creation / Definition:** Wrapping items inside `[...]` creates the list:
   ```python
   fruits = ["apple", "banana", "cherry"]
   ```
2. **Indexing (Accessing Elements):** Placing `[index]` immediately after the list variable accesses a specific element at that position:
   ```python
   print(fruits[0])  # 'apple'  (0-indexed: first item)
   print(fruits[1])  # 'banana' (second item)
   print(fruits[2])  # 'cherry' (third item)
   ```

> [!NOTE]
> **Square Brackets Contrast:**
> - In **Python code**, `[ ]` creates lists and indexes elements.
> - In **documentation**, `[ ]` denotes optional arguments (e.g., `round(number[, ndigits])`). In code, brackets are *never* optional!

---

### 8. The `for` Loop

While a `while` loop runs based on a conditional question, a **`for` loop** is designed to **iterate over a collection of items** (like a `list`).

#### A. Iterating Directly Over a `list`:
```python
for i in [0, 1, 2]:
    print("meow")
```
- **How it executes:**
  1. 1st pass: `i` is assigned `0` &rarr; prints `"meow"`.
  2. 2nd pass: `i` is assigned `1` &rarr; prints `"meow"`.
  3. 3rd pass: `i` is assigned `2` &rarr; prints `"meow"`.
  4. The list runs out of items &rarr; the loop terminates automatically!
- **Zero manual initialization or increments required!** Python automatically takes care of advancing through the list.

#### B. The Limitation of Manual Lists:
Hardcoding `[0, 1, 2]` works fine for 3 meows. But what if you need 1,000,000 meows?
Typing `[0, 1, 2, ..., 999999]` is impossible. That brings us to `range()`.

#### C. The `range()` Function:
Python provides a built-in function called **`range()`** that generates an arithmetic sequence of numbers on the fly:

```python
for i in range(3):
    print("meow")
```
- `range(3)` produces the sequence `0, 1, 2` (it stops **before** `3`, giving exactly 3 iterations).
- For a million meows: `for i in range(1000000):` (Python creates this efficiently without allocating a huge list in memory).

> [!WARNING]
> **`range()` Strictly Requires Integers (No Strings, No Floats!):**
> - `range()` **only accepts integers (`int`)**.
> - Passing a string causes an immediate crash:
>   ```python
>   for _ in range("3"):  # 💥 TypeError: 'str' object cannot be interpreted as an integer
>   ```
> - **The Common `input()` Gotcha:**
>   - Because `input()` always returns a `str`, you **must convert it with `int()`** before passing it into `range()`:
>     ```python
>     # ❌ CRASHES:
>     n = input("Number: ")
>     for _ in range(n): ...  # TypeError!
>
>     # ✅ CORRECT:
>     n = int(input("Number: "))
>     for _ in range(n): ...
>     ```

#### D. The Pythonic "Throwaway" Variable (`_`):
In the loop above, we never actually use the variable `i` inside the body (we just want to print `"meow"` 3 times).

In Python, if a loop variable is never referenced, the established convention is to name it **`_` (a single underscore)**:

```python
# The Pythonic way to say: "Repeat this 3 times, I don't care about the counter variable"
for _ in range(3):
    print("meow")
```

#### E. Iterating by Index: `range(len(students))`

In `hogwarts.py`, David Malan shows two fundamentally different ways to loop through a list of students:

##### Method 1: Direct Iteration (Iterate by Item)
When you only care about the values themselves:
```python
students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print(student)
```
- **Output:**
  ```text
  Hermoine
  Harry
  Ron
  ```

##### Method 2: Index-Based Iteration (`range(len(students))`)
What if you also need to know each student's **rank / position** (e.g. `1. Hermoine`, `2. Harry`, `3. Ron`)?  
You combine **`len()`** with **`range()`**:

```python
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```
- **Output:**
  ```text
  1 Hermoine
  2 Harry
  3 Ron
  ```

##### How the Inside-Out Evaluation Works:
1. **`len(students)`**: Returns `3` (the total number of items in the list).
2. **`range(3)`**: Evaluates to `0, 1, 2` (matching the valid 0-based indices!).
3. **`students[i]`**: Uses square bracket indexing to fetch the item at index `i`:
   - `i = 0` &rarr; `students[0]` &rarr; `"Hermoine"`
   - `i = 1` &rarr; `students[1]` &rarr; `"Harry"`
   - `i = 2` &rarr; `students[2]` &rarr; `"Ron"`
4. **`i + 1`**: Offsets the computer's 0-based index so humans see numbers starting from `1`!

---

### 9. Pythonic Shortcut: String Multiplication (`print("meow\n" * 3, end="")`)

David Malan shows a clever, loop-free trick unique to Python: **multiplying a string by an integer** (`str * int`).

#### Step 1: The Naive Multiplication Attempt
```python
print("meow" * 3)
```
- **Output:** `meowmeowmeow`
- **Problem:** All three meows are mashed together on one line with no spaces or newlines!

#### Step 2: Adding `\n` to Each Meow
```python
print("meow\n" * 3)
```
- **Output:**
  ```text
  meow
  meow
  meow

  ```
- **Problem:** Python's `print()` automatically appends its own default `end="\n"`. Because `"meow\n"` already has three newlines, plus `print()` adds a 4th, you get an **unwanted blank line** at the bottom!

#### Step 3: The Complete Solution (`end=""`)
To cancel `print()`'s default newline at the very end, set **`end=""`**:

```python
print("meow\n" * 3, end="")
```
- **Output (Exact & Clean):**
  ```text
  meow
  meow
  meow
  ```
- **Why this works:**
  1. `"meow\n" * 3` creates `"meow\nmeow\nmeow\n"`.
  2. `end=""` prevents `print()` from appending an extra newline after the 3rd meow.

### 10. Loop Control Statements: `continue` and `break`

Python provides two special control flow keywords to alter the standard behavior of loops on the fly:

| Keyword | What it Does | Analogy |
| :---: | :--- | :--- |
| **`continue`** | **Skips** the remainder of the *current* iteration and jumps straight to the next pass. | "Skip this round, keep playing." |
| **`break`** | **Immediately terminates** the *entire* loop and exits it completely. | "Stop the game and leave the room." |

---

### 11. User Input Validation Pattern: `while True` + `break`

In `cat.py`, David Malan wants the user to decide how many times the cat meows, but users might enter invalid numbers (like `-5` or `0`).

How do you force the user to provide a valid positive integer ($n > 0$)?  
The idiomatic Python pattern is an **infinite `while True` loop with a conditional `break`**:

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```

#### How this pattern executes:
1. `while True:` starts an infinite loop deliberately.
2. Prompts the user: `n = int(input(...))`
3. If the user enters a negative number or `0` (`n <= 0`):
   - The `if n > 0:` condition evaluates to `False`.
   - `break` is skipped!
   - Python loops back to step 1 and **prompts them again**.
4. As soon as the user enters a valid positive integer (e.g., `3`):
   - `n > 0` evaluates to `True`.
   - **`break` executes** &rarr; kicks execution out of the `while` loop immediately!
5. The `for _ in range(n):` loop takes over and prints `"meow"` 3 times.

---

### 12. Using `continue` for Explicit Filtering

`continue` restarts the loop immediately from the top, skipping any code below it in that iteration:

```python
while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue   # Skips directly back to the top of the while loop!
    else:
        break      # Valid number received -> exit loop!
```

- **Comparison:**
  - `break` says: *"I'm done with this loop forever."*
  - `continue` says: *"I'm done with this specific cycle; start the next cycle immediately."*

---

### 13. New Data Type: `dict` (Dictionaries)

As lists grow in complexity, associating two related pieces of data (e.g. each student with their Hogwarts house) becomes messy with separate lists.  
To solve this, David Malan introduces Python's **`dict` (dictionary)**.

#### A. What is a `dict`?
- **Definition:** An unordered collection of **key-value pairs** enclosed in curly braces **`{ }`**.
- Think of a real dictionary: you look up a **word (the key)** to find its **definition (the value)**.
- **Syntax:** `{"key": "value"}` separated by a colon `:` and comma-delimited:

```python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
```

#### B. Accessing Values: `print(students["Hermoine"])`
With a `list`, you look up items using integer indices: `students[0]`.  
With a `dict`, you look up items using **meaningful keys** inside square brackets `[ ]`:

```python
print(students["Hermoine"])  # Output: Gryffindor
print(students["Draco"])     # Output: Slytherin
```
- ⚠️ **KeyError:** If you search for a key that does not exist (e.g. `students["Voldemort"]`), Python crashes with a **`KeyError`**.

#### C. Looping Through a `dict`:
When you iterate through a dictionary with a `for` loop, Python automatically iterates through its **keys**:

```python
for student in students:
    print(student)
```
- **Output:**
  ```text
  Hermoine
  Harry
  Ron
  Draco
  ```

#### D. Printing Both Keys and Values Together:
To display both the student (key) and their house (value), use `student` as the key inside the loop:

```python
for student in students:
    print(student, students[student], sep=", ")
```
- **Output:**
  ```text
  Hermoine, Gryffindor
  Harry, Gryffindor
  Ron, Gryffindor
  Draco, Slytherin
  ```

---

### 14. Complex Data Structures: A List of Dictionaries

What if you have **more than two pieces of data** per entity?  
In `hogwarts.py`, David Malan introduces tracking 3 attributes for each student: **`name`**, **`house`**, and **`patronus`**.

To model this, you create a **`list` of `dict`s**:
```python
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
```

#### A. The `None` Keyword in Python:
- **`None`** is a special Python built-in constant and keyword that represents the **absence of a value** (similar to `null` in other languages).
- In the Harry Potter universe, Draco Malfoy does not possess a Patronus.
- Rather than putting an empty string `""` or omitting the key (which could cause a `KeyError`), setting `"patronus": None` explicitly signals: *"This field exists, but has no value."*
- ⚠️ **Capitalization:** Just like `True` and `False`, `None` must always be capitalized with a capital `N`.

#### B. Iterating Over a List of Dictionaries:
When looping through `students`, each iteration gives you one individual dictionary:

```python
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

- **Output:**
  ```text
  Hermoine, Gryffindor, Otter
  Harry, Gryffindor, Stag
  Ron, Gryffindor, Jack Russell terrier
  Draco, Slytherin, None
  ```

---

### 15. Nested Loops (Loops Within Loops) — The Mario Problem (`mario.py`)

In `mario.py`, David Malan uses the famous blocks from the Nintendo video game **Super Mario Bros.** to teach 1D and 2D iteration.

```text
    ?   Brick Block       #
  [?]   [?]   [?]       ###   Pyramid / Grid
```

#### Step 1: Printing a Vertical Column of Bricks (1D)
To print 3 bricks stacked vertically on top of each other:
```python
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
```
- **Output:**
  ```text
  #
  #
  #
  ```

#### Step 2: Printing a Horizontal Row of Bricks (1D with `end=""`)
To print 4 bricks side-by-side horizontally, we must prevent `print()` from automatically jumping to a new line after every brick:

```python
def main():
    print_row(4)

def print_row(width):
    print("?" * width)  # Or using a loop: for _ in range(width): print("?", end="")
    print()             # Prints a final newline after the row finishes

main()
```
- **Output:** `????`

---

#### Step 3: Printing a 2D Square Grid (A Loop Inside a Loop)
What if we want a **3x3 square grid of bricks**?

```text
###
###
###
```

A 2D grid requires **two dimensions**:
- **Rows** (moving vertically from top to bottom)
- **Columns** (moving horizontally from left to right across each row)

This requires a **Nested Loop** (an outer loop and an inner loop):

```python
def main():
    print_square(3)

def print_square(size):
    # Outer loop: Iterates through each ROW
    for i in range(size):
        # Inner loop: Iterates through each BRICK in that row
        for j in range(size):
            print("#", end="")
        # After completing a row, print a newline to move to the next row!
        print()

main()
```

##### How the Nested Loop Executes Step-by-Step:
1. **Outer loop starts at Row 0 (`i = 0`):**
   - Inner loop runs for `j = 0, 1, 2` &rarr; prints `###` with `end=""`.
   - Inner loop finishes.
   - `print()` runs &rarr; cursor moves to the next line!
2. **Outer loop moves to Row 1 (`i = 1`):**
   - Inner loop runs for `j = 0, 1, 2` &rarr; prints `###`.
   - `print()` moves to the next line.
3. **Outer loop moves to Row 2 (`i = 2`):**
   - Inner loop runs for `j = 0, 1, 2` &rarr; prints `###`.
   - `print()` moves to the next line.
4. Total bricks printed: $3 \times 3 = 9$.

---

#### Step 4: Simplifying the 2D Grid with Pythonic String Multiplication
David Malan also shows how Python's string multiplication can simplify the inner loop:

```python
def print_square(size):
    for _ in range(size):
        print("#" * size)
```
- The outer loop controls how many **rows** are printed.
- `print("#" * size)` replaces the entire inner loop in one clean, readable line!

---

## Code Examples & Patterns

```python
# 1. Standard while loop (cat.py)
i = 0
while i < 3:
    print("meow")
    i += 1

# 2. Countdown while loop
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")

# 3. For loop with a list
for i in [0, 1, 2]:
    print("meow")

# 4. For loop with range() and throwaway variable (_)
for _ in range(3):
    print("meow")

# 5. String multiplication shortcut without loops
print("meow\n" * 3, end="")

# 6. Input validation pattern using while True and break
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# 7. Iterating by index with range(len(...)) (hogwarts.py)
students = ["Hermoine", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

# 8. Dictionary mapping and iteration (hogwarts.py)
students_houses = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print("Lookup Hermoine:", students_houses["Hermoine"])

for student in students_houses:
    print(student, students_houses[student], sep=": ")

# 9. List of Dictionaries with 3 keys & None keyword (hogwarts.py)
students_data = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for s in students_data:
    print(s["name"], s["house"], s["patronus"], sep=", ")

# 10. Nested Loops: 2D Mario Square Grid (mario.py)
def print_grid(size):
    for i in range(size):          # Outer loop: rows
        for j in range(size):      # Inner loop: columns
            print("#", end="")
        print()                    # Line break after row completes

print_grid(3)
```

---

## Tips & Common Pitfalls

- **Off-By-One Errors:**
  - Starting at `i = 1` and checking `i <= 3` prints 3 times.
  - Starting at `i = 0` and checking `i <= 3` prints **4 times** (`0, 1, 2, 3`)! Prefer `i < 3` when starting at `0`.
- **Forgetting the Increment (`i += 1`):**
  - Always verify that every variable in the `while` condition changes inside the loop body, or it will loop infinitely.
- **Python Has No `i++`:**
  - Always write `i += 1`. Writing `i++` produces a `SyntaxError`.
