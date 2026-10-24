# CS50P — Lecture 1: Conditionals

- **Course:** Harvard CS50’s Introduction to Programming with Python
- **Instructor:** David J. Malan
- **Video:** [Watch Lecture 1 on YouTube](https://youtu.be/nLRL_NcnK-4?si=qANOfDsaaqo6DuOu)

---

## Key Concepts

### 1. What are Conditionals?
- **Definition:** Conditionals allow programs to make decisions and branch into different paths of execution based on whether a question/condition evaluates to `True` or `False`.
- They introduce the concept of **flow of control** — code no longer simply runs top-to-bottom on a single track.

---

### 2. Comparison Operators in Python

Comparison operators evaluate the relationship between two values and always return a **Boolean** (`bool`): either `True` or `False`.

| Operator | Meaning | Example | Evaluates To |
| :---: | :--- | :---: | :---: |
| **`>`** | Strictly Greater than | `5 > 3` | `True` |
| **`<`** | Strictly Less than | `2 < 1` | `False` |
| **`>=`** | Greater than or equal to | `5 >= 5` | `True` |
| **`<=`** | Less than or equal to | `4 <= 5` | `True` |
| **`==`** | Equality (Is equal to) | `5 == 5` | `True` |
| **`!=`** | Inequality (Is NOT equal to) | `5 != 3` | `True` |

#### The Fundamental Gotcha: `=` vs. `==`
- **`=` (Single Equals):** The **assignment operator**. It stores whatever is on the right into the variable on the left (`x = 5`).
- **`==` (Double Equals):** The **comparison operator**. It asks the question: *"Are these two values equal?"* and yields `True` or `False`.

```python
x = 5       # Stores 5 into x
x == 5      # Asks: Is x equal to 5? (True)
```

---

### 3. The `bool` (Boolean) Data Type

In addition to `str`, `int`, and `float`, Python includes a fundamental primitive type called **`bool`**.

#### A. Origin & Values
- Named after 19th-century English mathematician **George Boole** (inventor of Boolean algebra).
- A `bool` can only ever hold one of **two distinct values**:
  - `True`
  - `False`
- ⚠️ **Capitalization is Mandatory:** Python is case-sensitive. You must write `True` and `False` with capital `T` and `F`. Writing `true` or `false` produces a `NameError`.

#### B. The `bool()` Constructor
You can explicitly convert any value to a boolean using the `bool()` function:
```python
print(bool(1))       # Output: True
print(bool(0))       # Output: False
print(bool("cs50"))  # Output: True
print(bool(""))      # Output: False
```

#### C. "Truthy" vs. "Falsy" Values in Python
Every value in Python has an inherent boolean truth value when evaluated in a conditional statement:

| Category | **Falsy** (Evaluates to `False`) | **Truthy** (Evaluates to `True`) |
| :--- | :--- | :--- |
| **Numbers** | `0`, `0.0` | Any non-zero number (`1`, `-5`, `3.14`) |
| **Strings** | Empty string `""` | Any non-empty string (`"hello"`, `" "`) |
| **Special** | `None` | Objects, initialized values |
| **Collections** | Empty list `[]`, empty dict `{}` | Non-empty lists, tuples, dicts |

*Why this matters in conditionals:*
```python
name = input("What's your name? ")
if name:
    print(f"hello, {name}")
else:
    print("You didn't type anything!")
```

---

### 4. The `if` Statement (Branching)

The `if` statement evaluates a Boolean condition. If the condition is `True`, Python executes the indented block beneath it; if `False`, Python skips it entirely.

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```

- **Syntax Rules:**
  1. Starts with the `if` keyword.
  2. Followed by the condition (e.g., `x < y`). Parentheses are optional in Python.
  3. Ends with a colon `:`.
  4. The code to execute must be indented by **4 spaces**.

---

### 4. Mutually Exclusive Decisions: `elif` and `else`

In `compare.py`, David Malan demonstrates how programs evolve from inefficient multiple independent checks to mutually exclusive branches.

#### A. Inefficient: Multiple Independent `if` Statements
```python
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```
- **Why this is inefficient:**
  - Python is forced to evaluate **all 3 questions**, even if the first one was already `True`!
  - If $x < y$, it prints the message, but still wastes CPU cycles checking `x > y` and `x == y`.

#### B. Better: `if` and `elif` (Else If)
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```
- `elif` creates **mutually exclusive** branches: as soon as one condition evaluates to `True`, Python executes that block and **skips all subsequent `elif` statements**.

#### C. Best: `if`, `elif`, and `else`
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```
- **Why `else` is superior:**
  - By simple laws of logic: if $x$ is not less than $y$, and $x$ is not greater than $y$, then $x$ **must** be equal to $y$.
  - Asking `elif x == y` is redundant work. `else` acts as the universal fallback with **zero extra questions asked**.

### 5. Logical Operators (`or`, `and`, `not`)

Logical operators combine multiple Boolean expressions into a single compound condition.

| Operator | Rule | Example | Result |
| :---: | :--- | :---: | :---: |
| **`or`** | `True` if **at least one** operand is `True` | `x < y or x > y` | `True` if numbers differ |
| **`and`**| `True` only if **both** operands are `True` | `score >= 90 and score <= 100` | `True` for A grade |
| **`not`**| Inverts the Boolean value | `not (x == y)` | Same as `x != y` |

---

### 6. The `or` Operator & Code Simplification

In `compare.py`, David Malan refines checking whether two numbers are unequal:

#### Evolution of checking inequality:
```python
# Version 1: Using separate checks with elif
if x < y:
    print("x is not equal to y")
elif x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Version 2: Combining with 'or'
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Version 3: The Most Pythonic Way (using !=)
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

---

### 7. The `and` Operator & Chained Comparisons

In `grade.py`, David Malan shows how to check score ranges.

#### A. Using `and`:
```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

#### B. Chained Comparisons (Python Superpower!):
Python allows chaining comparisons just like in mathematics ($90 \le \text{score} \le 100$):
```python
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

#### C. Simplification via Elimination Order:
Because `elif` branches only execute if the previous branches were `False`, upper bounds are automatically guaranteed:
```python
# If score was >= 90, it would have stopped at the first 'if'!
# Therefore, in the second branch, score is already guaranteed to be < 90.
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

### 8. Short-Circuit Evaluation
Python evaluates compound conditions from left to right and stops as soon as the final outcome is determined:
- **`or`:** If the left side is `True`, Python **skips** evaluating the right side (the whole expression is already `True`).
- **`and`:** If the left side is `False`, Python **skips** evaluating the right side (the whole expression is already `False`).

---

### 9. Parity (`parity.py` & Modulo `%`)

**Parity** refers to whether an integer is **even** or **odd**.

#### A. The Math & The Modulo Operator (`%`)
- **Modulo (`%`)** yields the **remainder** after integer division.
- An even number divided by 2 leaves **no remainder** (`n % 2 == 0`).
- An odd number divided by 2 leaves a **remainder of 1** (`n % 2 != 0`).

```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 10. The Evolution of `is_even()` — Writing Pythonic Functions

In `parity.py`, David Malan demonstrates how to design a custom function that returns a Boolean (`True` or `False`).

#### Version 1: Novice (Verbose `if`/`else` with explicit returns)
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

#### Version 2: Intermediate — One-Line `return if else` (Python's Ternary Operator)
Python allows you to compress a standard multi-line `if`/`else` block into a **single, expressive line**:

```python
def is_even(n):
    return True if n % 2 == 0 else False
```

- **General Formula / Anatomy:**
  ```text
  return [VALUE_IF_TRUE] if [CONDITION] else [VALUE_IF_FALSE]
  ```
- **How Python Reads It:**
  1. Checks `[CONDITION]` first (`n % 2 == 0`).
  2. If `True`, returns `[VALUE_IF_TRUE]` (`True`).
  3. If `False`, returns `[VALUE_IF_FALSE]` (`False`).

- **Beyond Parity — Great Real-World Examples:**
  ```python
  # Returning a label based on age:
  status = "Adult" if age >= 18 else "Minor"

  # Absolute value function in one line:
  def absolute_value(n):
      return n if n >= 0 else -n

  # Greeting message in one line:
  def greet(name):
      return f"Hello, {name}" if name else "Hello, stranger"
  ```

#### Version 3: Master / Pythonic (Direct Boolean Evaluation)

This is David Malan's core punchline in `parity.py`:

> *"If a Boolean expression itself already evaluates to `True` or `False`, why bother asking `if` / `else` at all?"*

Look at what Version 1 and Version 2 are actually doing behind the scenes:
- *"If the expression is `True`, return `True`. If the expression is `False`, return `False`."*
- That is **100% redundant**! You are just returning the exact same truth value that the computer already calculated.

#### The Elegant One-Liner:
```python
def is_even(n):
    return n % 2 == 0
```

- **How Python Evaluates This Directly:**
  - When `n = 4`:
    - Python evaluates `4 % 2 == 0` &rarr; `0 == 0` &rarr; which produces `True`.
    - It hands `True` straight to `return`.
  - When `n = 5`:
    - Python evaluates `5 % 2 == 0` &rarr; `1 == 0` &rarr; which produces `False`.
    - It hands `False` straight to `return`.
- **Takeaway:** Never write `if condition == True: return True else: return False`. Simply write `return condition`!

#### Putting It Together with `main()`:
```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
```
*(Notice how readable `if is_even(x):` is — it reads just like spoken English!)*

---

### 11. The `match` Statement (Python 3.10+)

Introduced recently in **Python 3.10**, the `match` and `case` keywords provide **structural pattern matching** (similar to `switch` / `case` statements in languages like C, Java, and JavaScript).

#### A. Motivation: Replacing Chains of `if`/`elif`
In `house.py`, David Malan writes a program to determine which Hogwarts house a Harry Potter student belongs to:

```python
# The Traditional Way (if/elif/else):
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

#### B. The `match` Syntax:
With `match`, you specify the variable once, and list the possible `case` values beneath it:

```python
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

#### C. Combining Cases with the Pipe Operator (`|`)
Notice how Harry, Hermione, and Ron all belong to Gryffindor. Instead of writing three separate blocks, Python allows combining multiple cases using the vertical bar (`|`), which acts like `or`:

```python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

#### D. The Wildcard Pattern (`case _:`)
- The underscore **`_`** serves as a **wildcard** in Python.
- It matches **any value whatsoever** that didn't match the earlier cases.
- It is the direct equivalent of the fallback **`else:`** in an `if`/`elif` chain (or `default:` in other programming languages).

---

## Code Examples & Patterns

```python
# 1. Mutually Exclusive Flow (compare.py)
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# 2. Logical 'or' vs Inequality '!='
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# 3. Clean Range Checks (grade.py)
score = int(input("Score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Parity Check with Pythonic Boolean Function (parity.py)
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0  # Evaluates directly to True or False

main()

# 5. Pattern Matching with match / case (house.py)
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

---

## Tips & Common Pitfalls

- **Using `=` instead of `==` in conditions:**
  - `if x = y:` causes `SyntaxError: invalid syntax`. Always use `==` for comparison.
- **The Accidental Truthy Pitfall with `or`:**
  - ❌ `if x == "y" or "yes":` &rarr; Bug! Python evaluates `"yes"` as a non-empty string (`True`), so the condition is *always* `True`!
  - ✅ `if x == "y" or x == "yes":` or `if x in ["y", "yes"]:`
- **Indentation Matters:**
  - Indent with 4 spaces. Mixed tabs and spaces trigger `IndentationError`.
- **Take Advantage of Top-to-Bottom Elimination:**
  - When checking sequential ranges (like grades), order conditions from highest to lowest (or lowest to highest) to eliminate redundant `and` conditions.
