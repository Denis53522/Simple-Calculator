class Simple_Calculator:
    def __init__(self):
        pass

    def addition(self,first_number,second_number):
        return first_number + second_number # Adding first and second number

    def subtraction(self,first_number,second_number):
        return first_number - second_number # Subtracting first and second number

    def multiplication(self,first_number,second_number):
        return first_number * second_number # Multiplying first and second number

    def division(self,first_number,second_number):
        return first_number / second_number # Dividing first and second number

if __name__ == "__main__":
    calculator = Simple_Calculator()

    # Introduction
    print("\n=== Welcome to Simple Calculator! by Denis53522 ===")

    while True:
        try:
            first_number = float(input("\nEnter first number: ")) # Getting first number from user
            second_number = float(input("Enter second number: ")) # Getting second number from user
            operation = input("\n=== Operations ===\n1.) Addition\n2.) Subtraction\n3.) Multiplication\n4.) Division\nEnter operation: ") # Getting operation from user

            # Checking if the numbers are integers
            if first_number.is_integer():
                first_number = int(first_number)
            if second_number.is_integer():
                second_number = int(second_number)
            if operation == "1":
                result = calculator.addition(first_number,second_number)
                operation = "+"
            elif operation == "2":
                result = calculator.subtraction(first_number,second_number)
                operation = "-"
            elif operation == "3":
                result = calculator.multiplication(first_number,second_number)
                operation = "*"
            elif operation == "4":
                result = Simple_Calculator().division(first_number,second_number)
                operation = "/"
            else:
                print("Invalid operation must be between 1 and 4")
                continue

            if result.is_integer():
                result = int(result)

            print(f"\nAnswer: {first_number} {operation} {second_number} = {result}") # Printing result

            print("\nDo you want to continue?") # Asking user if they want to continue
            response = input("Enter yes or no: ").lower()
            if response == "no" or response == "n":
                print("Thank you for using Simple Calculator!")
                break
            elif response == "yes" or response == "y":
                continue
            else:
                print("Invalid response must be (yes/no) or (y/n)")
        except ValueError:
            print("Invalid input must be a number")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please try again.")
