# Python Control Statements — Deep Notes

# Introduction

Control statements are used to control the execution flow of a program.

By default, Python executes statements one by one from top to bottom.

Control statements change this normal flow based on:
- conditions
- loops
- jumps

They make programs:
- intelligent
- dynamic
- automated

---

# Why Control Statements Are Important

Without control statements:
- programs cannot make decisions
- programs cannot repeat tasks
- automation is impossible

Control statements are used in:
- banking systems
- login systems
- automation testing
- AI applications
- games
- web applications

---

# Types of Control Statements

| Type | Purpose |
|------|----------|
| Conditional Statements | Decision making |
| Looping Statements | Repeat execution |
| Jump Statements | Control loop behavior |

---

# 1. Conditional Statements

Conditional statements execute code based on conditions.

---

# Flow of Conditional Statements

```text
Condition Check
      ↓
True --------→ Execute if block
      ↓
False -------→ Execute else block
```

---

# Boolean Values

Conditional statements always work with Boolean values.

| Value | Meaning |
|------|----------|
| True | Condition satisfied |
| False | Condition failed |

---

# Truthy and Falsy Values

## Falsy Values

```python
False
0
None
""
[]
{}
()
```

Everything else is treated as True.

---

# if Statement

Executes block only when condition is True.

---

# Syntax

```python
if condition:
    statements
```

---

# Example

```python
temperature = 35

if temperature > 30:
    print("Hot Weather")
```

---

# Working Process

```text
Condition → temperature > 30
35 > 30 → True
Execute block
```

---

# Important Points

- Colon `:` is mandatory
- Indentation is mandatory
- Python uses indentation instead of braces

---

# Indentation

Correct:

```python
if True:
    print("Hello")
```

Wrong:

```python
if True:
print("Hello")
```

This gives:
```text
IndentationError
```

---

# if-else Statement

Used when there are two possible outcomes.

---

# Syntax

```python
if condition:
    statements
else:
    statements
```

---

# Example

```python
balance = 3000

if balance >= 5000:
    print("Withdrawal Allowed")

else:
    print("Insufficient Balance")
```

---

# Flow

```text
Condition True  → if block
Condition False → else block
```

---

# Real-Time Example

## Login System

```python
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")

else:
    print("Invalid Credentials")
```

---

# if-elif-else Statement

Used when multiple conditions exist.

---

# Syntax

```python
if condition:
    statements

elif condition:
    statements

else:
    statements
```

---

# Important Rule

Python checks conditions from top to bottom.

Once one condition becomes True:
- remaining conditions are skipped

---

# Example

```python
marks = 92

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

---

# Execution Flow

```text
marks = 92

92 >= 90 → True

Print Grade A

Stop remaining conditions
```

---

# Nested if Statement

if inside another if.

---

# Syntax

```python
if condition:

    if condition:
        statements
```

---

# Real-Time ATM Example

```python
account_active = True
balance = 12000

if account_active:

    amount = int(input("Enter Amount: "))

    if amount <= balance:

        if balance - amount >= 5000:

            balance = balance - amount

            print("Withdrawal Successful")
            print("Remaining Balance:", balance)

        else:
            print("Minimum balance should be 5000")

    else:
        print("Insufficient Balance")

else:
    print("Account Inactive")
```

---

# Logical Operators in Conditions

---

# AND Operator

All conditions must be True.

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

---

# OR Operator

Any one condition should be True.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

# NOT Operator

Reverses condition.

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

# Short-Circuit Evaluation

Python stops checking conditions once result is known.

---

# Example

```python
if True or 10/0:
    print("Hello")
```

Output:

```text
Hello
```

`10/0` is never checked because:
- `True or anything` = True

---

# 2. Looping Statements

Loops repeat code automatically.

---

# Why Loops Are Important

Without loops:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

With loops:

```python
for i in range(1, 6):
    print(i)
```

---

# Types of Loops

| Loop | Use |
|------|------|
| for | Known iterations |
| while | Unknown iterations |

---

# for Loop

Used when iterations are known.

---

# Syntax

```python
for variable in sequence:
    statements
```

---

# range() Function

Creates sequence of numbers.

---

# Types of range

## range(stop)

```python
range(5)
```

Output:
```text
0 1 2 3 4
```

---

## range(start, stop)

```python
range(1, 6)
```

Output:
```text
1 2 3 4 5
```

---

## range(start, stop, step)

```python
range(1, 10, 2)
```

Output:
```text
1 3 5 7 9
```

---

# Example

```python
for i in range(1, 6):
    print(i)
```

---

# while Loop

Runs until condition becomes False.

---

# Syntax

```python
while condition:
    statements
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Infinite Loop

```python
while True:
    print("Running")
```

---

# Real-Time Uses of Infinite Loops

- servers
- games
- chat applications
- automation tools

---

# Nested Loops

Loop inside another loop.

---

# Example

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

---

# Pattern Programs

```python
for i in range(5):

    for j in range(i + 1):
        print("*", end=" ")

    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

---

# 3. Jump Statements

Used to control loops.

---

# break Statement

Stops loop immediately.

---

# Example

```python
for i in range(1, 10):

    if i == 5:
        break

    print(i)
```

---

# continue Statement

Skips current iteration.

---

# Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

---

# pass Statement

Placeholder statement.

---

# Example

```python
if True:
    pass
```

---

# Difference Between break, continue, pass

| Statement | Purpose |
|------|----------|
| break | Stop loop |
| continue | Skip iteration |
| pass | Do nothing |

---

# Loop Else

Python supports else with loops.

---

# Example

```python
for i in range(5):
    print(i)

else:
    print("Loop Completed")
```

---

# Real-Time Examples of Control Statements

| Application | Usage |
|------|----------|
| ATM | Balance validation |
| Banking | Account verification |
| Login System | Authentication |
| E-commerce | Stock validation |
| Automation Testing | Test execution |
| AI Systems | Decision making |
| Games | User interaction |

---

# Common Interview Questions

## 1. Difference between if and while?

| if | while |
|----|--------|
| Executes once | Executes repeatedly |

---

## 2. Difference between break and continue?

| break | continue |
|--------|-----------|
| Stops loop | Skips iteration |

---

## 3. What is infinite loop?

A loop that never ends because condition always remains True.

---

# Best Practice Tips

- Avoid deep nested conditions
- Use meaningful variable names
- Avoid infinite loops unless required
- Keep conditions simple
- Use loops efficiently

---

# Summary

Control statements help programs:
- make decisions
- repeat tasks
- automate execution
- control flow

They are the foundation for:
- software development
- automation testing
- web development
- AI/ML
- backend systems
- real-time applications