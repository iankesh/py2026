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

### 5. Assignment Operators: `i += 1` vs `i = i + 1`

Python provides compound assignment operators as shorthand:
- **`i += 1`** is identical to **`i = i + 1`**
- **`i -= 1`** is identical to **`i = i - 1`**
- **`i *= 2`** is identical to **`i = i * 2`**
- ⚠️ **Note:** Python does **NOT** support `i++` or `i--` like C, C++, or Java!

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
