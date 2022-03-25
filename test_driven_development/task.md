Kata One - String Calculator
-
This kata was shamelessly stolen from https://codingdojo.org/kata/StringCalculator/

### Initial task
Create a function `add` that takes a String and returns a String:

    def add(input: str = None) -> str:

- An empty string will return “0”
- The method can take 0, 1 or 2 integer numbers separated by comma, and returns their sum
- Example of inputs: "", "1", "22,2"

Once that is done: Generalize to handle any number of arguments

### Extension

- Allow the add method to handle newlines as separators
- "1\n2,3" should return "6".
- "175,\n35" is invalid and should return the message "Number expected but '\n' found"
- "1,3," is invalid and should return the message Number expected but EOF found.
