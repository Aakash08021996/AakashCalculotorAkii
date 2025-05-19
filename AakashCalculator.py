import streamlit as st
import math

# App Title
st.title("🧮 Aakash Scientific Calculator")

# Number input
num1 = st.number_input("Enter first number:", format="%.4f")

# Operation selection
operation = st.selectbox(
    "Choose an operation:",
    [
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
        "Square Root (√x)",
        "Power (xʸ)",
        "Logarithm (log10)",
        "Sine (sin x)",
        "Cosine (cos x)",
        "Tangent (tan x)",
        "Exponential (eˣ)"
    ]
)

# For binary operations (need a second number)
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power (xʸ)"]:
    num2 = st.number_input("Enter second number:", format="%.4f")

# Result Calculation
result = None
if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("❌ Cannot divide by zero.")
        elif operation == "Square Root (√x)":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("❌ Cannot take square root of a negative number.")
        elif operation == "Power (xʸ)":
            result = math.pow(num1, num2)
        elif operation == "Logarithm (log10)":
            if num1 > 0:
                result = math.log10(num1)
            else:
                st.error("❌ Logarithm undefined for zero or negative numbers.")
        elif operation == "Sine (sin x)":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine (cos x)":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent (tan x)":
            result = math.tan(math.radians(num1))
        elif operation == "Exponential (eˣ)":
            result = math.exp(num1)

        if result is not None:
            st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
