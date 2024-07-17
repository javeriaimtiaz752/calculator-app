import streamlit as st
from cal_f1 import add
from cal_f2 import subtract
from cal_f3 import multiply
from cal_f4 import divide
st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operator = st.selectbox("Select operator", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        if num2 == 0:
            st.error("Cannot divide by zero")
        else:
            result = divide(num1, num2)

    st.success(f"Result: {result}")

if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator.")
                continue

            print("Result:", result)

            quit_choice = input("Quit calculator? (Y/N): ").upper()
            if quit_choice == 'Y':
                break

        except ValueError:
            print("Invalid input. Please enter numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")


