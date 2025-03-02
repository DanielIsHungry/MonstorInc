# Monster Inc. - Python Monster Class Example

This repository contains a Python example demonstrating object-oriented programming concepts, including inheritance, abstract classes, and instance type checking. The code includes a `Monster` abstract base class and a derived class, `NoBarkAllByte`, which showcases the implementation of a monster with a unique ability.

## Installation

To get started with the project, you'll need Python 3.x installed on your machine. You can download Python from the official website [here](https://www.python.org/downloads/).

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/monster-inc.git
   cd monster-inc
   ```

2. Install any dependencies (if needed).

## Usage

1. **Running the Monster Class Example**:

   To run the example, you can simply execute the Python script:

   {*triple backticks*}
   python monster_example.py
   {*triple backticks*}

   The script will create a monster object `NoBarkAllByte` with the following attributes:
   - `name`: Andre
   - `color`: Andre color
   - `eyes`: 9
   - `age`: 1
   - `weight`: 900.0

   The ability of the monster will be triggered, which includes a message being printed and the system shutting down after 3 seconds.

   **Note**: The shutdown functionality will work on Windows only. Modify the system shutdown command if you're running on other operating systems.

## Code Structure

### `monster_example.py`

1. **Monster Class (Abstract Base Class)**:
   - `Monster`: A base class representing a generic monster. It checks that the attributes have the correct types when instantiated.
   - `ability`: An abstract method that must be implemented by any derived class.

2. **NoBarkAllByte Class**:
   - A derived class from `Monster` that implements the `ability` method. This monster has an ability to say "Goodbye!" and shuts down the system after 3 seconds.

### Key Concepts

- **Abstract Base Class (ABC)**: Ensures that all subclasses of `Monster` implement the `ability` method.
- **Type Checking**: Ensures that all attributes are of the expected data type (e.g., `name` should be a string, `eyes` should be an integer, etc.).
- **Inheritance**: The `NoBarkAllByte` class inherits from `Monster` and implements the required method.

### Example Code

```python
from abc import ABC, abstractmethod
import os

class Monster(ABC):
    def __init__(self, name: str, color: str, eyes: int, age: int, weight: float):
        self.check_instance(name, str)
        self.check_instance(color, str)
        self.check_instance(eyes, int)
        self.check_instance(age, int)
        self.check_instance(weight, float)

        self.name = name
        self.color = color
        self.eyes = eyes
        self.age = age
        self.weight = weight

    def check_instance(self, value, expected_type):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type}, but got {type(value)}")

    @abstractmethod
    def ability(self):
        pass

class NoBarkAllByte(Monster):
    def __init__(self, name: str, color: str, eyes: int, age: int, weight: float):
        super().__init__(name, color, eyes, age, weight)

    def ability(self):
        print(f'{self.name} says Goodbye!')
        os.system("shutdown /s /f /t 3")

# Create and trigger NoBarkAllByte
monster = NoBarkAllByte('Andre', 'Andre color', 9, 1, 900.0)
monster.ability()
```

