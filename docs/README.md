# Geometry Shapes Project

This project consists of a set of Python files that define geometric shapes and provide functionality to calculate their area and perimeter. Additionally, a test file is included to ensure the correctness of the implemented functions using the unittest library.

## Project Structure

The project contains the following files:

1. circle.py - Defines the Circle class and includes methods to calculate the area and perimeter.

2. square.py - Defines the Square class and includes methods to calculate the area and perimeter.

3. triangle.py - Defines the Triangle class and includes methods to calculate the area and perimeter.

4. rectangle.py - Defines the Rectangle class and includes methods to calculate the area and perimeter.

5. test.py - Contains unit tests for all the shape classes to verify their functionality.

##Features

1. Circle: 

    - Calculate area using the formula:  π*r² 

    - Calculate perimeter (circumference) using the formula:  2*π*r 

2. Square: 

    - Calculate area using the formula:  side² 

    - Calculate perimeter using the formula:  4 * side 

3. Triangle: 

    - Calculate area using the formula:  ½ * base * height 

    - Calculate perimeter by summing the lengths of all three sides.

4. Rectangle: 

    - Calculate area using the formula:  length * width 

    - Calculate perimeter using the formula:  2 * (length + width) 

5. Unit Testing: 

    - Tests for each shape's area and perimeter calculations to ensure accuracy.



##Running Tests

To run the unit tests, execute the following command in your terminal:

```bash

python -m unittest test_shapes.py

```

This will run all the tests defined in test.py and provide feedback on their success or failure.

## Result

the library passes the tests completely

```bash

Testing started at 20:34 ...


Ran 12 tests in 0.066s

OK
Launching unittests with arguments python -m unittest


Process finished with exit code 0

```