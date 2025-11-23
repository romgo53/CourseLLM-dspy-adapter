# Programming Fundamentals and Data Types

## Introduction to Programming

Programming is the process of designing and building executable computer programs to accomplish specific computing tasks. At its core, programming involves problem-solving and logical thinking.

### Key Concepts

**Algorithm**: A step-by-step procedure for solving a problem or accomplishing a task. Algorithms must be:
- **Finite**: Must terminate after a finite number of steps
- **Definite**: Each step must be precisely defined
- **Input**: May have zero or more inputs
- **Output**: Must produce at least one output
- **Effective**: Each step must be basic enough to be executed

**Program**: An algorithm implemented in a programming language that can be executed by a computer.

## Variables and Data Types

### Primitive Data Types

**Integers (int)**
- Whole numbers without decimal points
- Examples: -5, 0, 42, 1000
- Typical operations: addition, subtraction, multiplication, division, modulo
- Memory: Usually 4 bytes (32 bits) or 8 bytes (64 bits)

**Floating-Point Numbers (float/double)**
- Numbers with decimal points
- Examples: 3.14, -0.001, 2.71828
- Trade-off between precision and range
- Important: Subject to rounding errors due to binary representation

**Boolean (bool)**
- Represents truth values
- Only two possible values: True or False
- Used extensively in conditional statements and loops
- Memory: Typically 1 byte

**Characters (char)**
- Single character or symbol
- Examples: 'a', 'Z', '5', '@'
- Stored using character encoding (ASCII, Unicode)
- Memory: 1 byte (ASCII) or more (Unicode)

**Strings (str)**
- Sequence of characters
- Examples: "Hello", "Computer Science", "12345"
- Can be manipulated using various string operations
- Immutable in many languages (like Python)

### Type Conversion

**Implicit Conversion (Coercion)**
- Automatic conversion by the compiler/interpreter
- Example: Adding int and float results in float

**Explicit Conversion (Casting)**
- Programmer-specified conversion
- Examples:
  - int("42") converts string to integer
  - float(10) converts integer to float
  - str(3.14) converts float to string

## Operators

### Arithmetic Operators
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Integer Division (//)
- Modulo (%)
- Exponentiation (**)

### Comparison Operators
- Equal to (==)
- Not equal to (!=)
- Greater than (>)
- Less than (<)
- Greater than or equal to (>=)
- Less than or equal to (<=)

### Logical Operators
- AND: Returns True only if both operands are True
- OR: Returns True if at least one operand is True
- NOT: Inverts the boolean value

### Operator Precedence
1. Parentheses ()
2. Exponentiation **
3. Unary +, -
4. Multiplication *, Division /, Modulo %
5. Addition +, Subtraction -
6. Comparison operators
7. Logical NOT
8. Logical AND
9. Logical OR

## Control Flow

### Sequential Execution
Programs execute line by line from top to bottom by default.

### Conditional Statements

**if Statement**
```
if condition:
    # execute if condition is True
```

**if-else Statement**
```
if condition:
    # execute if condition is True
else:
    # execute if condition is False
```

**if-elif-else Statement**
```
if condition1:
    # execute if condition1 is True
elif condition2:
    # execute if condition1 is False and condition2 is True
else:
    # execute if all conditions are False
```

### Loops

**While Loop**
- Repeats while a condition is True
- Pre-test loop (condition checked before execution)
- Risk: Infinite loops if condition never becomes False

```
while condition:
    # execute repeatedly while condition is True
```

**For Loop**
- Iterates over a sequence (range, list, string, etc.)
- Known number of iterations in advance (usually)

```
for variable in sequence:
    # execute for each item in sequence
```

### Loop Control Statements

**break**: Exits the loop immediately

**continue**: Skips the rest of the current iteration and moves to the next

**pass**: Does nothing, used as a placeholder

## Functions

### Function Definition
A function is a reusable block of code that performs a specific task.

**Components:**
- **Name**: Identifier for the function
- **Parameters**: Input values (optional)
- **Return value**: Output value (optional)
- **Body**: Code to execute

### Function Benefits
- **Modularity**: Break complex problems into smaller parts
- **Reusability**: Write once, use multiple times
- **Maintainability**: Easier to update and debug
- **Abstraction**: Hide implementation details

### Scope
- **Local scope**: Variables defined inside a function
- **Global scope**: Variables defined outside all functions
- **LEGB Rule** (Python): Local → Enclosing → Global → Built-in

## Input/Output

### Input
- Reading data from user, files, or other sources
- Must often be converted to appropriate data type

### Output
- Displaying results to user or writing to files
- Formatting output for readability

## Comments and Documentation

### Comments
- Single-line comments: Explain specific lines
- Multi-line comments: Explain complex sections
- Should explain "why" not just "what"

### Documentation
- Function docstrings: Explain purpose, parameters, return value
- Module-level documentation: Overview of program
- Good documentation is essential for maintenance

## Best Practices

1. **Use meaningful variable names**: `student_count` not `x`
2. **Follow naming conventions**: snake_case or camelCase consistently
3. **Keep functions small and focused**: One task per function
4. **Avoid magic numbers**: Use named constants
5. **Handle errors gracefully**: Don't assume perfect input
6. **Test thoroughly**: Check edge cases and boundary conditions
7. **Comment wisely**: Explain complex logic, not obvious code
8. **Write readable code**: Proper indentation and spacing

## Common Errors

### Syntax Errors
- Violations of language grammar rules
- Detected at compile/parse time
- Examples: Missing colons, unmatched parentheses

### Runtime Errors
- Occur during program execution
- Examples: Division by zero, invalid type operations

### Logical Errors
- Program runs but produces incorrect results
- Hardest to find and fix
- Require careful testing and debugging

## Debugging Strategies

1. **Print statements**: Display variable values
2. **Debugger**: Step through code line by line
3. **Rubber duck debugging**: Explain code to someone/something
4. **Binary search**: Narrow down where error occurs
5. **Unit tests**: Test individual functions in isolation
