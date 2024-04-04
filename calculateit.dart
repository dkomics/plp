import 'dart:io';

void main() {
  // Display a welcome message
  print("Simple Calculator");

  // Prompt the user to enter the first number and read input
  print("Enter the first number: ");
  double num1 = double.parse(stdin.readLineSync()!);

  // Prompt the user to enter the second number and read input
  print("Enter the second number: ");
  double num2 = double.parse(stdin.readLineSync()!);

  // Display available operations
  print("Select an operation:");
  print("1. Addition (+)");
  print("2. Subtraction (-)");
  print("3. Multiplication (*)");
  print("4. Division (/)");

  // Read the user's choice of operation
  int choice = int.parse(stdin.readLineSync()!);

  // Perform the selected operation based on user input
  switch (choice) {
    case 1:
      // If user chooses addition, call the add function and print the result
      print("Result: ${add(num1, num2)}");
      break;
    case 2:
      // If user chooses subtraction, call the subtract function and print the result
      print("Result: ${subtract(num1, num2)}");
      break;
    case 3:
      // If user chooses multiplication, call the multiply function and print the result
      print("Result: ${multiply(num1, num2)}");
      break;
    case 4:
      // If user chooses division, check if the denominator is zero, then call divide function and print result
      if (num2 != 0) {
        print("Result: ${divide(num1, num2)}");
      } else {
        // If denominator is zero, display an error message
        print("Error: Division by zero is not allowed.");
      }
      break;
    default:
      // If user enters an invalid choice, display an error message
      print("Invalid choice. Please enter a number between 1 and 4.");
  }
}

// Function to perform addition
double add(double a, double b) => a + b;

// Function to perform subtraction
double subtract(double a, double b) => a - b;

// Function to perform multiplication
double multiply(double a, double b) => a * b;

// Function to perform division
double divide(double a, double b) => a / b;
