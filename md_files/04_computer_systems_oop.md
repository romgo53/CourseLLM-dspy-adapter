# Computer Systems and Object-Oriented Programming

## Computer Architecture Fundamentals

### The Von Neumann Architecture

Modern computers follow the Von Neumann architecture, consisting of:

1. **Central Processing Unit (CPU)**
   - Control Unit: Coordinates operations, fetches instructions
   - Arithmetic Logic Unit (ALU): Performs calculations and logical operations
   - Registers: Small, fast storage locations inside CPU

2. **Memory (RAM - Random Access Memory)**
   - Stores programs and data being actively used
   - Volatile: Contents lost when power is off
   - Directly addressable by CPU
   - Organized as sequence of bytes

3. **Input/Output (I/O) Devices**
   - Input: Keyboard, mouse, sensors, network
   - Output: Monitor, printer, speakers, network

4. **Bus**
   - Communication pathway between components
   - Data bus: Carries data
   - Address bus: Carries memory addresses
   - Control bus: Carries control signals

### How Programs Execute

**Fetch-Decode-Execute Cycle:**

1. **Fetch**: CPU retrieves instruction from memory at address in Program Counter (PC)
2. **Decode**: Control unit interprets instruction
3. **Execute**: ALU performs operation
4. **Store**: Result written back to memory or register
5. **Repeat**: PC updated to next instruction

**Clock Speed:**
- Measured in GHz (billions of cycles per second)
- Higher clock = more instructions per second
- Not the only factor in performance (architecture matters)

### Memory Hierarchy

From fastest to slowest:

1. **CPU Registers**
   - Smallest, fastest
   - Accessed in < 1 clock cycle
   - Typically 8-128 bytes total

2. **Cache Memory (L1, L2, L3)**
   - L1: Fastest, smallest (32-64 KB per core)
   - L2: Medium (256 KB - 1 MB per core)
   - L3: Shared, larger (2-32 MB)
   - Stores frequently accessed data

3. **RAM (Main Memory)**
   - 4-64+ GB typical
   - Access time: ~100 CPU cycles
   - Volatile

4. **Secondary Storage (SSD/HDD)**
   - Persistent storage
   - Much larger (256 GB - several TB)
   - Much slower than RAM
   - Non-volatile

5. **Network Storage**
   - Cloud storage, network drives
   - Slowest access
   - Potentially unlimited capacity

**Principle of Locality:**
- **Temporal locality**: Recently accessed data likely to be accessed again
- **Spatial locality**: Data near recently accessed data likely to be accessed soon
- Caching exploits these principles

## Number Systems and Data Representation

### Binary System

**Definition**: Base-2 number system using only 0 and 1.

**Why Binary?**
- Electronic circuits have two states: on/off, high/low voltage
- Reliable and simple
- Boolean logic maps directly to circuits

**Converting Decimal to Binary:**
```
Example: 13 to binary
13 ÷ 2 = 6 remainder 1  (LSB)
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1  (MSB)

Result: 1101
```

**Converting Binary to Decimal:**
```
1101 = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
     = 8 + 4 + 0 + 1
     = 13
```

### Bits, Bytes, and Words

- **Bit**: Single binary digit (0 or 1)
- **Byte**: 8 bits (standard unit)
- **Word**: CPU's natural data size (32 or 64 bits typically)

**Storage Units:**
- 1 KB (kilobyte) = 1,024 bytes = 2¹⁰ bytes
- 1 MB (megabyte) = 1,024 KB = 2²⁰ bytes
- 1 GB (gigabyte) = 1,024 MB = 2³⁰ bytes
- 1 TB (terabyte) = 1,024 GB = 2⁴⁰ bytes

### Hexadecimal System

**Definition**: Base-16 system using 0-9 and A-F.

**Why Hexadecimal?**
- Compact representation of binary
- One hex digit = 4 binary digits
- Easy conversion to/from binary

**Hex Digits:**
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A(10), B(11), C(12), D(13), E(14), F(15)

**Examples:**
- Binary 1111 = Hex F
- Binary 1010 = Hex A
- Binary 11011101 = Hex DD

### Representing Integers

**Unsigned Integers:**
- All bits represent magnitude
- Range for n bits: 0 to 2ⁿ-1
- 8 bits: 0 to 255
- 16 bits: 0 to 65,535

**Signed Integers (Two's Complement):**
- Most significant bit (MSB) is sign bit
- Positive: Same as unsigned
- Negative: Two's complement representation

**Two's Complement Process:**
```
To represent -5 in 8 bits:
1. Write +5: 00000101
2. Invert bits: 11111010
3. Add 1: 11111011
Result: -5 = 11111011
```

**Advantages:**
- Single zero representation
- Addition/subtraction work the same for signed/unsigned
- Simple hardware implementation

**Range for n bits:** -2ⁿ⁻¹ to 2ⁿ⁻¹-1
- 8 bits: -128 to 127
- 16 bits: -32,768 to 32,767

### Representing Real Numbers

**Floating-Point Representation (IEEE 754):**

Components:
- **Sign bit**: 0 for positive, 1 for negative
- **Exponent**: Biased representation of power
- **Mantissa (Significand)**: Fractional part

**Single Precision (32 bits):**
- 1 sign bit
- 8 exponent bits
- 23 mantissa bits
- Range: ±1.4×10⁻⁴⁵ to ±3.4×10³⁸

**Double Precision (64 bits):**
- 1 sign bit
- 11 exponent bits
- 52 mantissa bits
- Greater precision and range

**Limitations:**
- Not all real numbers can be represented exactly
- Rounding errors accumulate
- Special values: NaN (Not a Number), Infinity

### Character Encoding

**ASCII (American Standard Code for Information Interchange):**
- 7 bits per character (128 characters)
- Includes letters, digits, punctuation, control characters
- Example: 'A' = 65, 'a' = 97, '0' = 48

**Unicode:**
- Universal character set
- Supports all world languages
- UTF-8, UTF-16, UTF-32 encodings
- UTF-8: Variable length, backward compatible with ASCII
- Example: 'A' = U+0041, '😀' = U+1F600

## Programming Paradigms

### Procedural Programming

**Characteristics:**
- Program is series of procedures/functions
- Focus on sequence of steps to perform
- Data and functions are separate
- Examples: C, Pascal, early BASIC

**Advantages:**
- Straightforward and intuitive
- Good for small to medium programs
- Efficient execution

**Disadvantages:**
- Hard to maintain large programs
- Data can be accessed globally (potential bugs)
- Limited reusability

### Object-Oriented Programming (OOP)

**Definition**: Programming paradigm based on objects that contain data (attributes) and code (methods).

**Core Principles:**

#### 1. Encapsulation

**Definition**: Bundling data and methods that operate on that data within a single unit (class), and restricting access to internal details.

**Benefits:**
- Data hiding: Control access to internal state
- Modularity: Changes to implementation don't affect outside code
- Easier maintenance: Clear interface boundaries

**Implementation:**
- Private attributes: Hidden from outside
- Public methods: Interface to interact with object
- Getters/setters: Controlled access to private data

**Example Concept:**
```
Class BankAccount:
    Private: balance
    Public: deposit(amount)
    Public: withdraw(amount)
    Public: get_balance()
```

Users can't directly modify balance, must use methods.

#### 2. Inheritance

**Definition**: Mechanism where a new class (child/subclass) derives properties and behavior from existing class (parent/superclass).

**Benefits:**
- Code reusability: Don't repeat common code
- Hierarchical classification: Models real-world relationships
- Extensibility: Add features without modifying existing code

**Types:**
- **Single inheritance**: One parent class
- **Multiple inheritance**: Multiple parent classes (not all languages)
- **Multilevel inheritance**: Chain of inheritance (A→B→C)

**Example Concept:**
```
Class Animal:
    eat(), sleep()

Class Dog inherits Animal:
    bark()
    Inherits: eat(), sleep()
```

**"Is-a" Relationship**: Dog IS-AN Animal

#### 3. Polymorphism

**Definition**: Ability of objects of different types to respond to the same method call in different ways.

**Types:**

**Compile-time Polymorphism (Overloading):**
- Same method name, different parameters
- Resolved at compile time
```
add(int a, int b)
add(float a, float b)
add(int a, int b, int c)
```

**Runtime Polymorphism (Overriding):**
- Subclass provides specific implementation of parent method
- Resolved at runtime
```
Class Animal:
    speak(): print("Some sound")

Class Dog inherits Animal:
    speak(): print("Bark")

Class Cat inherits Animal:
    speak(): print("Meow")
```

**Benefits:**
- Flexibility: Same interface, different implementations
- Extensibility: Add new types without changing existing code
- Dynamic behavior: Behavior determined at runtime

#### 4. Abstraction

**Definition**: Hiding complex implementation details and showing only essential features.

**Benefits:**
- Reduces complexity: Users only see what they need
- Increases security: Implementation hidden
- Easier to understand and use

**Implementation:**
- Abstract classes: Cannot be instantiated, provide template
- Interfaces: Contract specifying methods that must be implemented

**Example Concept:**
```
Abstract Class Shape:
    Abstract method: calculate_area()

Class Circle inherits Shape:
    Implements: calculate_area() using πr²

Class Rectangle inherits Shape:
    Implements: calculate_area() using length×width
```

Users know all shapes can calculate area, don't need to know how.

## Classes and Objects

### Class

**Definition**: Blueprint or template for creating objects.

**Components:**
- **Attributes (Properties/Fields)**: Data stored in objects
- **Methods (Functions)**: Behavior of objects
- **Constructor**: Special method to initialize objects

**Example Structure:**
```
Class Car:
    Attributes:
        make, model, year, color, speed
    
    Constructor:
        Initialize make, model, year, color
        Set speed to 0
    
    Methods:
        accelerate()
        brake()
        turn()
        get_speed()
```

### Object

**Definition**: Instance of a class - concrete entity created from class blueprint.

**Creating Objects:**
```
my_car = new Car("Toyota", "Camry", 2024, "Blue")
your_car = new Car("Honda", "Civic", 2023, "Red")
```

Each object has its own:
- Set of attribute values
- Access to class methods

### Attributes vs. Methods

**Attributes (Instance Variables):**
- Represent state/data of object
- Each object has its own copy
- Example: car's color, person's name

**Methods (Member Functions):**
- Represent behavior/actions
- Shared by all instances of class
- Operate on object's attributes
- Example: car.accelerate(), person.speak()

### Class vs. Instance

**Class Attributes:**
- Shared by all instances
- Belong to class itself
- Example: Car.number_of_wheels = 4

**Instance Attributes:**
- Unique to each instance
- Belong to specific object
- Example: my_car.color = "Blue"

**Class Methods:**
- Operate on class, not instance
- Cannot access instance attributes
- Example: Factory methods

**Instance Methods:**
- Operate on specific instance
- Can access instance attributes
- Example: my_car.accelerate()

## Software Development Concepts

### Modularity

**Definition**: Dividing program into separate, independent modules.

**Benefits:**
- Easier to understand: Smaller, focused components
- Easier to test: Test modules independently
- Easier to maintain: Changes isolated to modules
- Reusability: Modules can be used in multiple programs
- Parallel development: Different developers work on different modules

**Principles:**
- **High cohesion**: Module's parts are closely related
- **Low coupling**: Minimal dependencies between modules

### Code Reusability

**Techniques:**
- Functions: Reusable blocks of code
- Classes: Reusable object templates
- Inheritance: Extend existing functionality
- Libraries: Collections of reusable code
- Design patterns: Proven solutions to common problems

**Benefits:**
- Faster development
- Fewer bugs: Tested code reused
- Consistency: Same implementation everywhere
- Easier maintenance: Fix once, fixed everywhere

### Software Testing

**Types of Testing:**

1. **Unit Testing**
   - Test individual functions/methods
   - Automated, fast
   - Example: Test that add(2, 3) returns 5

2. **Integration Testing**
   - Test interaction between modules
   - Ensure components work together
   - Example: Test database and UI interaction

3. **System Testing**
   - Test complete system
   - Verify requirements are met
   - Example: Test entire e-commerce workflow

4. **Acceptance Testing**
   - Verify system meets user needs
   - Often performed by users
   - Determines if software is ready for deployment

**Test-Driven Development (TDD):**
1. Write test first (it fails)
2. Write minimal code to pass test
3. Refactor code while keeping test passing

## Version Control

**Purpose**: Track changes to code over time, enable collaboration.

**Key Concepts:**
- **Repository**: Storage for project and its history
- **Commit**: Snapshot of changes
- **Branch**: Independent line of development
- **Merge**: Combine changes from different branches

**Git Workflow:**
1. Make changes to code
2. Stage changes (mark for commit)
3. Commit changes (save snapshot)
4. Push to remote repository (share with others)

**Benefits:**
- Track history: See what changed and why
- Collaboration: Multiple developers work simultaneously
- Branching: Experiment without affecting main code
- Rollback: Revert to previous versions

## Software Design Principles

### DRY (Don't Repeat Yourself)

**Principle**: Every piece of knowledge should have a single, unambiguous representation.

**How to Apply:**
- Extract repeated code into functions
- Use inheritance to share common behavior
- Use configuration files instead of hardcoded values

### KISS (Keep It Simple, Stupid)

**Principle**: Simplicity should be a key goal; unnecessary complexity avoided.

**How to Apply:**
- Write clear, readable code
- Avoid over-engineering
- Use straightforward solutions
- Choose simplicity over cleverness

### YAGNI (You Aren't Gonna Need It)

**Principle**: Don't add functionality until it's actually needed.

**How to Apply:**
- Implement features when required, not "just in case"
- Avoid speculative generality
- Focus on current requirements

### SOLID Principles

1. **Single Responsibility**: Class should have one reason to change
2. **Open/Closed**: Open for extension, closed for modification
3. **Liskov Substitution**: Subclass should be substitutable for parent
4. **Interface Segregation**: Many specific interfaces better than one general
5. **Dependency Inversion**: Depend on abstractions, not concretions

## Error Handling

### Types of Errors

1. **Syntax Errors**: Code violates language rules
2. **Runtime Errors**: Occur during execution (e.g., division by zero)
3. **Logical Errors**: Code runs but produces wrong results

### Exception Handling

**Concept**: Separate error handling code from normal flow.

**Components:**
- **try**: Code that might raise exception
- **catch/except**: Handle specific exceptions
- **finally**: Code that always executes (cleanup)
- **throw/raise**: Manually trigger exception

**Benefits:**
- Cleaner code: Error handling separate from logic
- Robust programs: Graceful handling of unexpected situations
- Debugging: Better error messages

**Best Practices:**
- Catch specific exceptions, not general ones
- Don't use exceptions for normal flow control
- Provide meaningful error messages
- Clean up resources in finally block

## Summary

Understanding computer systems and OOP principles is fundamental to modern software development:

- **Computer Architecture**: Hardware foundation of computing
- **Data Representation**: How information is stored and manipulated
- **OOP**: Powerful paradigm for organizing complex software
- **Software Engineering**: Practices for building reliable, maintainable systems

These concepts build on each other to enable development of sophisticated software systems.
