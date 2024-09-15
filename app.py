import streamlit as st

# Simple calculator logic
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else 'Error (Division by Zero)'

# Streamlit UI
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
operation = st.selectbox("Choose operation", ['+', '-', '*', '/'])

# Calculate result on button click
if st.button("Calculate"):
    result = calculator(num1, num2, operation)
    st.write(f"The result of {num1} {operation} {num2} = {result}")
