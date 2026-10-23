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
    - *(Note: `[chars]` is in square brackets in documentation, indicating it is **optional** — omit it to strip whitespace by default).*
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

- **The `calculator.py` Case Study: Fixing String Concatenation (`x + y`):**

  1. **The Bug — String Concatenation:**
     When writing a basic calculator, beginners naturally try:
     ```python
     x = input("What's x? ")  # User enters: 1
     y = input("What's y? ")  # User enters: 2
     z = x + y
     print(z)                 # Output: "12" (BUG!)
     ```
     - **Why this happens:** Because `input()` *always* returns a `str` (string). When Python sees the `+` operator between two strings, it performs **string concatenation** (gluing text together: `"1"` + `"2"` = `"12"`), not mathematical addition!

  2. **Approach 1: Convert when calculating (`int(x) + int(y)`):**
     Keep `x` and `y` as strings initially, then cast them when computing:
     ```python
     x = input("What's x? ")
     y = input("What's y? ")
     z = int(x) + int(y)      # 1 + 2 = 3
     print(z)                 # Output: 3
     ```

  3. **Approach 2: Nesting Functions — `int(input(...))` (Best Practice):**
     Instead of creating temporary string variables, you pass the `input()` function call directly inside `int()`:
     ```python
     x = int(input("What's x? "))
     y = int(input("What's y? "))
     print(x + y)             # Output: 3
     ```

- **Deep Dive: Nested Functions (Function Composition):**
  - **Definition:** A nested function occurs when the call to one function serves as the argument to another:
    ```python
    outer_function(inner_function())
    ```
  - **The Inside-Out (Onion Layer) Rule:**
    - Python evaluates nested functions **strictly from the innermost parentheses outward**:
      ```text
      x = int( input("What's x? ") )
               \_________________/   1. INNER function runs first -> prompts user & returns "5" (str)
             \___________________/   2. OUTER function runs next  -> int("5") converts it to 5 (int)
      x = 5                          3. Assignment '=' stores final integer 5 into variable x
      ```

  - **Multi-Level Nesting Examples:**
    - **2 Levels:** `print(square(4))` &rarr; `square(4)` returns `16`, then `print(16)` executes.
    - **3 Levels:** `score = round(float(input("Score: ")), 2)`
      1. `input(...)` returns `"98.6666"`
      2. `float(...)` converts to `98.6666`
      3. `round(..., 2)` rounds to `98.67`

  - **Nested Functions vs. Method Chaining:**
    - **Nested Functions (Inside-Out):** `int(input("x: "))` &rarr; Wrap functions inside functions like an onion.
    - **Method Chaining (Left-to-Right):** `name.strip().title()` &rarr; Calls object methods in sequence using dot notation.

  - **Readability & The "Too Much Nesting" Rule:**
    - Nesting 1 to 2 levels (e.g., `int(input(...))` or `print(f"...")`) is clean and eliminates unnecessary dummy variables.
    - **Over-nesting** hurts readability and debugging:
      ```python
      # Avoid over-nesting on one line (hard to read and debug):
      print(round(float(input("x: ")) + float(input("y: ")), 2))
      ```

  - ⚠️ **`ValueError` with Nested `int(input())`:**
    - If user types letters (e.g. `"cat"`), the inner `input()` succeeds, but the outer `int("cat")` immediately crashes:
      `ValueError: invalid literal for int() with base 10: 'cat'`

#### C. The `float` (Floating-Point) Data Type

- **Definition:** Represents real numbers containing a **decimal point** (e.g., `3.14`, `-0.01`, `0.0`, `100.5`).
  - Called "floating-point" because the decimal point can "float" depending on how many significant digits exist before and after it.

- **Casting Input with `float()`:**
  - Unlike `int()`, which crashes on decimals, `float()` parses numbers with fractional values:
    ```python
    x = float(input("What's x? "))  # User enters: 1.5
    y = float(input("What's y? "))  # User enters: 2.5
    print(x + y)                    # Output: 4.0
    ```

- **Division Always Yields a `float`:**
  - In Python 3, the single-slash division operator `/` **always returns a `float`**, even if the numbers divide evenly without a remainder:
    ```python
    print(10 / 2)  # Output: 5.0 (float, not int 5)
    print(2 / 3)   # Output: 0.6666666666666666
    ```

- **Floating-Point Imprecision:**
  - Computers store numbers in memory as binary (base-2: 0s and 1s), not base-10 decimals.
  - Just as the fraction $1/3$ cannot be represented precisely with finite base-10 decimals ($0.3333...$), fractions like $0.1$ and $0.2$ cannot be represented precisely in binary.
  - **The Classic Example:**
    ```python
    print(0.1 + 0.2)  # Output: 0.30000000000000004 (not exactly 0.3!)
    ```

- **The `round()` Function Deep Dive:**
  - Python includes a built-in `round()` function to manage decimal precision:
    ```python
    round(number[, ndigits])
    ```
  - **Understanding Python Documentation Syntax — Square Brackets `[ ]` Mean "Optional":**
    - In Python's official documentation, square brackets `[ ]` indicate that an argument is **optional** (you do not have to provide it).
    - `number` has no brackets around it &rarr; **required** (you must provide at least one number).
    - `[, ndigits]` is in brackets &rarr; **optional** (you can omit it, or provide an integer specifying decimal places).
    - **Why is the comma inside the bracket `[, ndigits]`?**
      - It signals: *"If you choose to supply `ndigits`, you must also include the comma separating it from `number`."*
    - ⚠️ **Critical Rule:** Never type the square brackets in actual Python code! They are purely documentation notation.
      ```python
      # ❌ SYNTAX ERROR / creates a list:
      round(3.14159, [2])

      # ✅ CORRECT:
      round(3.14159, 2)
      ```
    - *(You also see this pattern in string methods like `str.strip([chars])`, where `chars` is optional!)*

  - **1. Rounding to the Nearest Integer (when `ndigits` is omitted):**
    ```python
    print(round(2.6))  # Output: 3
    print(round(2.1))  # Output: 2
    ```
  - **2. Rounding to Specific Decimal Places (`ndigits`):**
    ```python
    z = 2 / 3
    print(round(z, 2))  # Output: 0.67
    ```
  - **3. Python's Rounding Rule — Banker's Rounding (Round Half to Even):**
    - When a number ends exactly in `.5` (equidistant from two integers), Python rounds to the **nearest EVEN number**:
      ```python
      print(round(2.5))  # Output: 2  (2 is even)
      print(round(3.5))  # Output: 4  (4 is even)
      ```
    - *Why?* Standard "round half up" creates an upward bias in financial/scientific computations. Rounding half to even balances rounding errors symmetrically.

- **`round()` vs. f-string Formatting (`:.2f`):**

  | Feature | `round(z, 2)` | `f"{z:.2f}"` |
  | :--- | :--- | :--- |
  | **Return Type** | A numerical `float` (`12.5`) | A formatted text `str` (`"12.50"`) |
  | **Trailing Zeros** | Drops trailing zeros (`12.50` &rarr; `12.5`) | **Enforces** exact decimal places (`"12.50"`) |
  | **Thousands Commas**| Not supported directly | Supported via `f"{z:,.2f}"` (`"1,234.50"`) |
  | **Best Used For** | Mathematical calculations | Displaying to users / printing currency |

#### D. Type Conversion (Type Casting)

**Type Conversion** (also universally called **Type Casting**) is the process of converting a value from one data type into another (for example, taking the string `"5"` and converting it into the integer `5`).

1. **Explicit Type Conversion (Type Casting):**
   - When the programmer manually tells Python to convert a value using built-in conversion functions:
     - **`int(x)`**: Converts `x` to an integer (e.g., `int("42")` &rarr; `42`, or `int(3.9)` &rarr; `3` [truncates decimals]).
     - **`float(x)`**: Converts `x` to a floating-point decimal (e.g., `float("3.14")` &rarr; `3.14`, or `float(5)` &rarr; `5.0`).
     - **`str(x)`**: Converts `x` to a string (e.g., `str(50)` &rarr; `"50"`).
     - **`bool(x)`**: Converts `x` to boolean `True` or `False` (e.g., `bool(0)` &rarr; `False`, `bool(1)` &rarr; `True`).

2. **Implicit Type Conversion (Type Coercion):**
   - When Python automatically converts data types behind the scenes without manual intervention, usually to avoid losing precision during arithmetic:
     - Adding an `int` and a `float`:
       ```python
       a = 3       # int
       b = 2.5     # float
       c = a + b   # Python automatically converts 'a' to 3.0 -> c is 5.5 (float)
       ```
     - Float division with `/`:
       ```python
       result = 4 / 2  # Python automatically converts result to 2.0 (float)
       ```

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

- **What does the "f" stand for?**
  - The `f` stands for **format** — which is why they are called **Format Strings** (or *formatted string literals* in the official Python docs).
- **How David Malan Introduces It in CS50:**
  - In `hello.py`, you start by combining strings with `print()` in two basic ways:
    1. Using concatenation (`+`): `print("hello, " + name)` *(requires manual spacing and only works with strings)*
    2. Using comma arguments: `print("hello,", name)` *(uses `print()`'s default separator)*
  - Then, David introduces **f-strings** as Python's modern, elegant solution:
    ```python
    name = input("What's your name? ")
    print(f"hello, {name}")
    ```
- **Why are they called format strings?**
  - They allow you to **format** variables directly inside the string using curly braces `{}` rather than breaking the string apart with commas or `+` signs.

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
After your variable inside `{}` , adding a colon `:` signals that you want to apply **formatting specifications**:

- **Thousands Separator (`:,`):**
  - **In CS50 (`calculator.py`):** When adding large numbers (like `x = 1000` and `y = 0` or large sums), David Malan demonstrates how to add commas automatically:
    ```python
    z = 1000
    print(f"{z:,}")  # Output: 1,000
    ```
  - Works on both integers and floats:
    ```python
    z = 1000000
    print(f"{z:,}")  # Output: 1,000,000
    ```
  - **Underscore Separator (`:_`):**
    - You can also use an underscore for readability: `print(f"{1000000:_}")` &rarr; `1_000_000`.
  - **Country / Regional Formatting (Locales):**
    - The standard `:,` always uses the Anglo-American comma standard (groups of 3).
    - If you need European formatting (where `.` is used for thousands and `,` for decimals) or Indian numbering systems (lakhs/crores), Python provides the `locale` module (`f"{z:n}"` with locale set). In CS50, `f"{z:,}"` is the standard tool taught.

- **Decimal Precision (`:.Nf`):**
  - Rounds to $N$ decimal places and formats as a float:
    ```python
    z = 2 / 3           # 0.6666666666666666...
    print(f"{z:.2f}")   # Output: 0.67 (automatically rounded!)
    ```
  - **Breaking Down the Syntax `:.2f`:**
    | Character | Meaning |
    | :--- | :--- |
    | **`:`** | Starts the formatting instructions |
    | **`.`** | Targets the decimal digits |
    | **`2`** | Enforces exactly **2** decimal places |
    | **`f`** | Formats as a **f**loating-point number |
  - **The Superpower: Preserves Trailing Zeros (Unlike `round()`):**
    - `round(50.5, 2)` drops trailing zeros &rarr; prints `50.5`
    - `f"{50.5:.2f}"` **forces** 2 digits &rarr; prints `50.50` (essential for displaying currency like dollars/cents!)

- **Combined Commas & Decimals (`:,.2f`):**
  - Combines both thousands commas and 2 fixed decimal places:
    ```python
    z = 1250000.5
    print(f"${z:,.2f}")  # Output: $1,250,000.50
    ```

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

# 6. Data Types: float, round(), and Formatting
x = float(input("Enter decimal x: "))          # e.g., 2.5
y = float(input("Enter decimal y: "))          # e.g., 1.2
print(f"Float Sum ({x} + {y}): {x + y}")

# Division produces float
z = 2 / 3
print(f"Raw division (2 / 3): {z}")            # 0.6666666666666666
print(f"round(z, 2):          {round(z, 2)}")  # 0.67
print(f"Formatted ':.2f':     {z:.2f}")        # '0.67'

# Banker's Rounding (Round half to even)
print(f"round(2.5): {round(2.5)}")             # 2 (nearest even number)
print(f"round(3.5): {round(3.5)}")             # 4 (nearest even number)

# Currency formatting with commas and fixed decimals
price = 1250000.5
tax = 0.05
total = price * (1 + tax)
print(f"Total Price: ${total:,.2f}")           # Output: $1,312,500.50

# 7. Functions with 'return' (Reusable & Composable)
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
