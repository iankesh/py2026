# CS50P — Lecture 0: Functions, Variables

- **Course:** Harvard CS50’s Introduction to Programming with Python
- **Instructor:** David J. Malan
- **Video:** [Watch Lecture 0 on YouTube](https://youtu.be/nLRL_NcnK-4?si=qANOfDsaaqo6DuOu)

---

## Key Concepts

### 1. Functions
- **Definition:** A reusable block of code that performs a specific action. You can think of functions as verbs in programming.
- **Built-in Functions:** Provided by Python out of the box, such as `print()`, `input()`, `int()`, `float()`, `round()`, and `type()`.
- **Calling / Invoking:** Running a function by writing its name followed by parentheses: `function_name()`.
- **Custom Functions:** Defined using the `def` keyword, allowing you to create your own reusable actions.

---

### 2. Variables & Assignment (`variable = input()`)
- **What is a Variable?**
  - A named container or storage location in computer memory that holds data so you can use, modify, or refer to it later.
- **How Assignment Works: `variable = input(...)`**
  - The single equals sign `=` is the **assignment operator** (not mathematical equality; equality in Python is `==`).
  - **Evaluated from Right to Left:**
    1. The computer executes the right side first: `input("What's your name? ")` prompts the user, waits for them to type, and returns that text as a string (e.g., `"Alice"`).
    2. Python then stores that returned value into the variable on the left side (`name`).
  - *Mental Model:*
    ```text
    name  <--- [stores value] <---  input("What's your name? ")  ["Alice"]
    ```
- **Reassigning & Updating Variables:**
  - You can overwrite a variable's value with an updated version of itself:
    ```python
    name = input("Name: ")
    name = name.strip()       # Removes accidental spaces
    name = name.title()       # Capitalizes words
    ```
- **PEP 8 Naming Conventions:**
  - Use `snake_case` (all lowercase with underscores): `first_name`, `total_price`.
  - Must begin with a letter or underscore `_`, **never a number** (`1name` is invalid; `name1` is valid).
  - Variable names are **case-sensitive** (`name`, `Name`, and `NAME` are distinct).

---

### 3. Data Types (`str`, `int`, `float`)

In Python, every value has a **data type** that dictates what kind of data it represents and what operations can be performed on it. You can check any value's type using the `type()` function (e.g., `type("hello")` &rarr; `<class 'str'>`).

#### A. The `str` (String) Data Type
- **Definition:** Text represented as an ordered sequence of characters enclosed in quotes (`"..."` or `'...'`).
- **Strings are Immutable:**
  - In Python, strings cannot be changed in place.
  - Any string method returns a **brand new string**; it does not modify the original. You must reassign the variable to keep changes: `name = name.strip()`.
- **The Strip Methods Family (`.strip()`, `.lstrip()`, `.rstrip()`):**
  Python provides three variations for trimming characters from string boundaries:

  | Method | Direction | What It Does | Example (`"   hello   "`) | Output |
  | :--- | :--- | :--- | :--- | :--- |
  | **`str.strip()`** | **Both ends** | Trims characters from the **start AND end** | `"   hello   ".strip()` | `'hello'` |
  | **`str.lstrip()`** | **Left only** | Trims characters from the **start (left side)** only | `"   hello   ".lstrip()` | `'hello   '` |
  | **`str.rstrip()`** | **Right only** | Trims characters from the **end (right side)** only | `"   hello   ".rstrip()` | `'   hello'` |

  - **1. `.strip([chars])`:**
    - Removes whitespace or specified characters from **both ends**.
    - ⚠️ **Important:** It **never removes whitespace inside or between words**:
      ```python
      "   David     Malan   ".strip()  # Output: "David     Malan"
      ```

  - **2. `.lstrip([chars])` (Left Strip):**
    - The `"l"` stands for **Left**. It removes characters only from the beginning (left) of the string.
    - Spaces or characters on the right are preserved completely.
    - *Common Use Cases:*
      - Stripping leading indentation / spaces: `"    code".lstrip()` &rarr; `"code"`
      - Stripping leading zeroes: `"00042".lstrip("0")` &rarr; `"42"`
      - Stripping leading URL protocols: `"https://cs50.harvard.edu".lstrip("https://")` &rarr; `"cs50.harvard.edu"`

  - **3. `.rstrip([chars])` (Right Strip):**
    - The `"r"` stands for **Right**. It removes characters only from the end (right) of the string.
    - Spaces or characters on the left are preserved completely.
    - *Common Use Cases:*
      - Stripping trailing newlines (`\n`) when reading files: `"hello\n".rstrip("\n")` &rarr; `"hello"`
      - Stripping trailing slashes from file paths or URLs: `"folder/subfolder/".rstrip("/")` &rarr; `"folder/subfolder"`
      - Cleaning trailing spaces after typing.

  - **Stripping Custom Characters:**
    - If you pass an argument to any of these methods, Python treats it as a **set of characters to remove** (in any order) until it hits a character not in the set:
      ```python
      "...hello...".lstrip(".")  # Output: "hello..."
      "...hello...".rstrip(".")  # Output: "...hello"
      "...hello...".strip(".")   # Output: "hello"
      ```
- **The `.capitalize()` vs. `.title()` Methods:**

  | Method | What It Does | Example Input | Output | Best Used For |
  | :--- | :--- | :--- | :--- | :--- |
  | **`str.capitalize()`** | Capitalizes **only the first character** of the entire string; converts all other characters to lowercase. | `"david malan"` | `"David malan"` | Single words or sentences |
  | **`str.title()`** | Capitalizes the first character of **every word**; converts remaining letters in each word to lowercase. | `"david malan"` | `"David Malan"` | Full names, titles, headings |

  - **Why `.capitalize()` is not enough for names:**
    - If the user types `"david malan"`, `.capitalize()` produces `"David malan"`. The last name `"malan"` remains lowercase because it only modifies the very first letter of the string.
    - `.title()` solves this by capitalizing both `"David"` and `"Malan"`.
  - **Handling Irregular / Mixed Casing:**
    - Both methods automatically fix accidental uppercase letters:
      - `"dAvId mAlAn".capitalize()` &rarr; `"David malan"`
      - `"dAvId mAlAn".title()` &rarr; `"David Malan"`
- **Other Essential String Methods:**
  - `.lower()` / `.upper()`: Converts entire string to lowercase or uppercase.

- **Splitting Strings & Multiple Variable Unpacking (`first, last = name.split(" ")`):**
  - **What `.split([sep])` Does:**
    - Breaks a single string into a **list of smaller strings** based on a specified delimiter (separator).
    - If `sep=" "` is passed: `"David Malan".split(" ")` &rarr; `["David", "Malan"]`.
    - If called with no arguments `name.split()`: automatically splits by any whitespace (spaces, tabs, newlines) and discards duplicate/consecutive spaces.
  - **Multiple Variable Assignment (Unpacking):**
    - You can assign the parts directly into multiple variables on the left side of `=`:
      ```python
      name = "David Malan"
      first, last = name.split(" ")
      print(f"First: {first}, Last: {last}")
      ```
    - *Mental Model:*
      ```text
      "David Malan".split(" ")  -->  ["David",  "Malan"]
                                        |          |
                                        v          v
                                      first       last
      ```
  - **All-in-One Chaining with `input()`:**
    ```python
    first, last = input("Enter first and last name: ").strip().title().split(" ")
    ```
  - ⚠️ **The `ValueError` Unpacking Gotcha:**
    - The number of variables on the left **must exactly match** the number of items produced by `.split()`:
      - If user types `"David"` (1 word) &rarr; `ValueError: not enough values to unpack (expected 2, got 1)`
      - If user types `"David J. Malan"` (3 words) &rarr; `ValueError: too many values to unpack (expected 2, got 3)`
    - *(Later in the course, conditionals and error handling are used to guard against this).*

- **Method Chaining (`.strip().capitalize()` or `.strip().title()`):**
  - Because string methods return a **new string**, you can immediately invoke another string method on that result by chaining them with dots (`.`):
  - **The 3-Step Progression (from verbose to clean):**
    1. *Separate lines:*
       ```python
       name = input("What's your name? ")
       name = name.strip()
       name = name.capitalize()
       ```
    2. *Chained on the variable:*
       ```python
       name = input("What's your name? ")
       name = name.strip().capitalize()
       ```
    3. *Chained directly on `input()` (Single Line):*
       ```python
       name = input("What's your name? ").strip().capitalize()
       ```
  - **How Python Evaluates This (Left-to-Right):**
    1. `input("What's your name? ")` prompts user &rarr; returns `"  david  "` (a `str`).
    2. `.strip()` runs on that string &rarr; returns `"david"` (a new `str`).
    3. `.capitalize()` runs on `"david"` &rarr; returns `"David"` (the final `str`).
    4. `=` stores `"David"` into `name`.

#### B. The `int` (Integer) Data Type
- **Definition:** Represents **whole numbers** without any decimal or fractional part.
  - Can be positive, negative, or zero: `... -3, -2, -1, 0, 1, 2, 3 ...`
  - In Python 3, integers have arbitrary precision (they can grow as large as memory allows without integer overflow).

- **Arithmetic Operators (`+`, `-`, `*`, `/`, `%`):**

  | Operator | Name | What It Does | Example | Result | Notes |
  | :---: | :--- | :--- | :--- | :---: | :--- |
  | **`+`** | **Addition** | Adds two numbers together | `5 + 3` | `8` | On strings, `+` concatenates (`"5" + "3"` &rarr; `"53"`). |
  | **`-`** | **Subtraction** | Subtracts right operand from left | `10 - 4` | `6` | Supports negative results (`3 - 5` &rarr; `-2`). |
  | **`*`** | **Multiplication** | Multiplies two numbers | `4 * 3` | `12` | On strings, `*` repeats text (`"ha" * 3` &rarr; `"hahaha"`). |
  | **`/`** | **Division** | Divides left by right | `10 / 2` | `5.0` | ⚠️ **Always returns a `float`**, even if evenly divisible! |
  | **`%`** | **Modulo (Remainder)** | Returns remainder after division | `10 % 3` | `1` | `3 * 3 = 9`, remainder is `1`. |

- **Related Division Operators in Python:**
  - **`//` (Floor / Integer Division):** Divides and rounds down to the nearest whole integer, dropping any decimal remainder:
    - `10 // 3` &rarr; `3`
  - **`**` (Exponentiation / Power):** Raises base to exponent:
    - `2 ** 3` &rarr; `8` (2 cubed)

- **The Modulo Operator (`%`) Deep Dive:**
  - **Core Concept:** Gives you whatever is left over after dividing as many whole times as possible:
    - `7 % 3` &rarr; `1` (3 goes into 7 twice = 6; remainder = 1)
    - `8 % 4` &rarr; `0` (4 goes into 8 evenly; remainder = 0)
  - **Primary Real-World Use Case — Even vs. Odd Check:**
    - Any number `% 2 == 0` is **Even**.
    - Any number `% 2 != 0` is **Odd**.

- **Type Casting User Input to `int` (`int()`):**
  - Because `input()` always returns a string, adding two `input()` results directly causes string concatenation:
    ```python
    x = input("x: ")  # User types 1
    y = input("y: ")  # User types 2
    print(x + y)      # Output: "12" (String Concatenation!)
    ```
  - **The Fix:** Explicitly cast with `int()`:
    ```python
    x = int(input("x: "))  # 1
    y = int(input("y: "))  # 2
    print(x + y)           # Output: 3 (Mathematical Addition!)
    ```
  - ⚠️ **`ValueError` Gotcha:** Passing text with letters or decimals to `int()` raises an error:
    - `int("cat")` &rarr; `ValueError: invalid literal for int() with base 10: 'cat'`
    - `int("3.14")` &rarr; `ValueError: invalid literal for int() with base 10: '3.14'` (use `float("3.14")` instead).

#### C. The `float` (Floating-Point) Data Type
- **Definition:** Real numbers that include a decimal point (e.g., `3.14`, `-0.01`, `2.0`).
- **Floating-Point Imprecision:** Computers store decimals in binary (base-2), which can lead to tiny rounding anomalies (e.g., `0.1 + 0.2` might equal `0.30000000000000004`).
- **The `round()` Function:**
  - `round(number[, ndigits])`: Rounds a number to a specified number of decimal digits.
  - If `ndigits` is omitted, rounds to the nearest whole integer:
    ```python
    z = round(3.14159, 2)  # Output: 3.14
    ```

#### D. Type Conversion (Type Casting)
- `int(value)`: Converts value to an integer (drops decimals if given a float).
- `float(value)`: Converts value to a floating-point number.
- `str(value)`: Converts any value into its text string representation.

---

### 4. Arguments vs. Parameters
- **Parameter:** The placeholder variable listed in the function definition:
  ```python
  def greet(name):  # 'name' is a parameter
      print(f"hello, {name}")
  ```
- **Argument:** The actual value passed into the function when calling it:
  ```python
  greet("David")    # "David" is an argument
  ```
- **Positional Arguments:** Values assigned based on their position/order (`print("Hello,", name)`).
- **Keyword Arguments:** Values assigned by name, typically with default values (`print(..., sep=" ", end="\n")`).

---

### 5. Deep Dive: `print()` Parameters (Official Python Docs)

From the official Python documentation (`docs.python.org`), the signature for `print()` is:

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

- **`*objects` (Positional):**
  - You can pass zero, one, or multiple values separated by commas.
  - Python automatically converts each object into a string using `str()`. If no objects are passed (`print()`), it prints a blank line.
- **`sep=' '` (Separator Keyword):**
  - Specifies what string to insert **between** multiple objects.
  - Defaults to a single space `' '`.
  - Use `sep=""` to combine items without spaces, or `sep=", "` for comma-separated outputs.
- **`end='\n'` (End Character Keyword):**
  - Specifies what string to append **after** the last object.
  - Defaults to `'\n'` (newline, which pushes the cursor to the next line).
  - Use `end=""` to keep the subsequent `print()` on the **same line**.
- **`file=None` (Output Destination):**
  - Specifies where text is written. Defaults to `None`, which means `sys.stdout` (the terminal screen).
  - Can be redirected to a file (`file=f`) or error stream (`file=sys.stderr`).
- **`flush=False` (Buffer Flushing):**
  - Output to the screen is usually buffered in memory until a newline or full buffer occurs.
  - Setting `flush=True` forces Python to display the output **immediately**, which is essential for real-time progress bars or timers.

---

### 6. Multiple Inverted Commas & The Backslash (`\`)

#### A. Multiple Inverted Commas on a Single Line
1. **Alternating Inverted Commas (Single vs. Double):**
   - Wrap in `' '` if `"` is inside: `print('She said "yes" and he said "no"')`
   - Wrap in `" "` if `'` is inside: `print("It's a sunny day, isn't it?")`
2. **Triple Inverted Commas (`"""` or `'''`) on a Single Line:**
   - Written on one single line to hold both `'` and `"` without escaping:
     ```python
     print("""He said, "It's fine!" """)
     ```
   - ⚠️ **The 4-Quote Gotcha:** Avoid `""""` at the end by adding a space: `"""... " """` or escaping `"""...\""""`.
3. **Implicit String Concatenation on a Single Line:**
   - Adjacent strings placed next to each other are auto-merged:
     ```python
     print("hello, " 'world, ' "it's Python!")  # hello, world, it's Python!
     ```

#### B. The Backslash (`\`) — The Escape Character
The backslash tells Python to treat the following character literally or specially:
- `\"` &rarr; Literal double quote (`"`)
- `\'` &rarr; Literal single quote (`'`)
- `\\` &rarr; Literal backslash (`\`)
- `\n` &rarr; Newline
- `\t` &rarr; Horizontal tab
- **Line Continuation (`\` at line end):** Splits long code lines across multiple lines without error.
- **Raw Strings (`r"..."`):** Disables escape interpretation (e.g., `print(r"C:\new_folder\test")`).

---

### 7. Format Strings (f-strings) & `{}` Placeholders

Introduced in Python 3.6, **f-strings** (formatted string literals) provide the cleanest and fastest way to interpolate variables into text.

#### A. Basic Syntax
Prefix the opening quote with an `f` or `F`. Any variable or expression inside `{}` is evaluated and inserted directly:
```python
name = "David"
print(f"hello, {name}")   # Output: hello, David
```

#### B. What Can Go Inside `{}`?
- **Variables:** `f"Instructor: {first} {last}"`
- **Inline Expressions & Math:** `f"Next year: {age + 1}"`
- **Method & Function Calls:** `f"Clean: {name.strip().title()}"`

#### C. Formatting Modifiers (The Colon `:` Syntax)
- **Thousands Separator (`:,`):** `f"{1000000:,}"` &rarr; `1,000,000`
- **Decimal Precision (`:.Nf`):** `f"{3.14159:.2f}"` &rarr; `3.14`
- **Combined (`:,.2f`):** `f"${1250000.5:,.2f}"` &rarr; `$1,250,000.50`
- **Literal Braces `{{` and `}}`:** `f"Set: {{{name}}}"` &rarr; `Set: {David}`

---

### 8. Side Effects vs. Return Values
- **Side Effect:** Any action a function performs outside its own internal scope besides returning data.
  - *Example:* Printing text to the screen using `print()` is a **side effect**.
  - *Important:* `print()` displays text on the console, but its return value is `None`. You cannot store its output for math calculations.
- **Return Value:** The actual data a function passes back to the program using `return`.
  - *Example:* `input()` returns a string you can save in a variable and manipulate.

---

### 9. The `return` Keyword
- **Definition:** Hands a calculated result back to the caller and **immediately terminates** the function.
- **Why use `return` instead of `print()`?**
  - **Composability:** You can pass the returned value into another function (`print(square(4))`), store it in a variable, or use it in math equations (`square(3) + square(4)`).
  - **Reusability & Testing:** Returning values allows automated unit tests to verify correctness without needing console output.
- **Unreachable Code:** Any code written directly after `return` within the same block will never run.
- **Implicit Return:** If a function finishes without an explicit `return`, it returns `None` by default.
- **Multiple Returns:** You can return multiple values separated by commas: `return width, height` (returned as a tuple).

---

## Code Examples & Patterns

```python
# 1. Multiple Inverted Commas on a Single Line & Backslash Escape
# (a) Alternating quotes on a single line
print('She said "yes" and he said "no"')       # Double quotes inside single quotes
print("It's a sunny day, isn't it?")           # Single quotes/apostrophes inside double quotes

# (b) Triple quotes on a single line (Note space before closing """ to avoid 4 quotes)
print("""He said, "It's Python time!" """)

# (c) Implicit single-line concatenation
print("hello, " 'world, ' "it's Python!")      # Automatically combined into one string

# (d) Backslash escape sequences
print("She said, \"hello, friend\"")           # Escaped double quotes
print('It\'s working!')                        # Escaped single quote
print("Line 1\nLine 2\tIndented tab")          # Newline \n and Tab \t
print("Folder path: C:\\Users\\CS50")          # Literal backslash \\

# (e) Raw string (disables escape interpretation)
print(r"C:\new_folder\test")                   # \n is NOT treated as newline

# 2. Using print() Parameters (sep, end, file, flush)
print("2026", "10", "19", sep="-")            # Output: 2026-10-19
print("hello", "world", sep="")               # Output: helloworld
print("Connecting", end="...")
print("Connected!")                            # Output: Connecting...Connected!

# 3. Format Strings (f-strings) with {} and Modifiers
name = "David"
age = 20
print(f"hello, {name}! Next year you will be {age + 1}.")

# Thousands separator (:,) and fixed decimal precision (:.2f)
balance = 1250000.758
print(f"Balance: ${balance:,.2f}")             # Output: $1,250,000.76
print(f"Variable {{name}} holds: {name}")       # Output: Variable {name} holds: David

# 4. Data Types: str Methods (.strip, .capitalize, .title)
raw_input = "   David Malan\n   "
print(f"Original: '{raw_input}'")
print(f"strip():   '{raw_input.strip()}'")        # Removes leading & trailing whitespace
print(f"lstrip():  '{raw_input.lstrip()}'")       # Removes left whitespace only
print(f"rstrip():  '{raw_input.rstrip()}'")       # Removes right whitespace only

# Comparing .capitalize() vs .title()
user_entry = "david malan"
print(f"capitalize(): '{user_entry.capitalize()}'") # Output: 'David malan' (last name stays lowercase)
print(f"title():      '{user_entry.title()}'")      # Output: 'David Malan' (both words capitalized)

# Stripping custom characters from edges
code = "00042"
print(f"lstrip('0'): '{code.lstrip('0')}'")        # Output: '42'

path = "cs50/python/"
print(f"rstrip('/'): '{path.rstrip('/')}'")        # Output: 'cs50/python'

url = "...https://cs50.harvard.edu/..."
print(f"Custom strip: '{url.strip('.')}'")        # Output: 'https://cs50.harvard.edu/'

# Method Chaining directly on input()
first_name = input("Enter first name: ").strip().capitalize()
full_name = input("Enter full name: ").strip().title()
print(f"First Name (.strip().capitalize()): {first_name}")
print(f"Full Name  (.strip().title()):      {full_name}")

# Splitting and Unpacking into multiple variables
name = "David Malan"
first, last = name.split(" ")
print(f"Unpacked -> First: '{first}', Last: '{last}'")

# All-in-one: input() + .strip() + .title() + .split(" ")
first, last = input("Enter first & last name: ").strip().title().split(" ")
print(f"Hello {first}, your surname is {last}!")

# 5. Data Types: int & Arithmetic Operators (+, -, *, /, %, //, **)
a = 10
b = 3

print(f"Addition ({a} + {b}):           {a + b}")    # 13
print(f"Subtraction ({a} - {b}):        {a - b}")    # 7
print(f"Multiplication ({a} * {b}):     {a * b}")    # 30
print(f"Division ({a} / {b}):           {a / b}")    # 3.3333333333333335 (Always a float!)
print(f"Floor Division ({a} // {b}):    {a // b}")   # 3 (Truncates decimals)
print(f"Modulo / Remainder ({a} % {b}): {a % b}")    # 1 (Remainder after division)
print(f"Power ({a} ** {b}):             {a ** b}")   # 1000 (10 to the 3rd power)

# Practical Modulo Use-Case: Even vs. Odd
num = int(input("Enter an integer to test even/odd: "))
if num % 2 == 0:
    print(f"{num} is Even (num % 2 == 0)")
else:
    print(f"{num} is Odd (num % 2 != 0)")

price = float(input("Enter price: "))
tax = float(input("Enter tax (e.g. 0.05): "))
total = round(price * (1 + tax), 2)
print(f"Total: ${total:,.2f}")

# 6. Functions with 'return' (Reusable & Composable)
def square(n):
    """Calculates and returns the square of n."""
    return n * n

result = square(5)                             # 25
print("Square of 5:", result)
print("3^2 + 4^2 =", square(3) + square(4))    # 9 + 16 = 25
```

---

## Tips & Common Pitfalls

- **`input()` Always Returns `str`:**
  - For numeric math, wrap `input()` in `int()` or `float()`. Adding two strings (`"1" + "2"`) produces `"12"`.
- **String Immutability:**
  - `name.strip()` does not alter `name`. You must reassign: `name = name.strip()`.
- **`.strip()` Does Not Remove Inner Spaces:**
  - `"  a   b  ".strip()` results in `"a   b"`. It only trims the outer edges.
- **Confusing `print()` with `return`:**
  - `print()` shows output to the user (side effect). `return` hands data back to code. `x = print(...)` makes `x == None`.
- **Floating-Point Imprecision:**
  - Decimal calculations in computers can yield tiny inaccuracies; use `round(value, ndigits)` or f-string formatting (`:.2f`).
- **Unterminated String Literals:**
  - Starting with `'` and closing with `"` causes `SyntaxError: unterminated string literal`. Ensure quotes match or use escape backslashes `\`.
