


# # print("\nWelcome to the Unit Converter App\n")

# # conversions_available = [
# #     (1, "Kilometers", "Miles"),
# #     (2, "Miles", "Kilometers"),
# #     (3, "Kilograms", "Pounds"),
# #     (4, "Pounds", "Kilograms"),
# #     (5, "Inches", "Centimeters"),
# #     (6, "Centimeters", "Inches"),
# #     (7, "Fahrenheit", "Celsius"),
# # ]

# # print("Conversions available:\n")
# # for conversion_number, from_unit, to_unit in conversions_available:
# #     print(f"{conversion_number}. {from_unit} to {to_unit}")

# # # Get user input safely
# # while True:
# #     conversion = input("\nEnter the number of the conversion to use --> ").strip()
# #     if conversion.isdigit():
# #         conversion_index = int(conversion) - 1
# #         if 0 <= conversion_index < len(conversions_available):
# #             break
# #         else:
# #             print("Invalid choice. Please enter a valid number from the list.")
# #     else:
# #         print("Invalid input. Please enter a number.")

# # # Extract conversion details
# # conversion_number, from_unit, to_unit = conversions_available[conversion_index]

# # # Get the value to convert
# # while True:
# #     try:
# #         from_value = float(input(f"\nEnter the value in {from_unit} --> "))
# #         break
# #     except ValueError:
# #         print("Invalid input. Please enter a numeric value.")

# # # Perform the conversion
# # if conversion_number == 1:  # Kilometers to Miles
# #     to_value = from_value * 0.621371
# # elif conversion_number == 2:  # Miles to Kilometers
# #     to_value = from_value / 0.621371
# # elif conversion_number == 3:  # Kilograms to Pounds
# #     to_value = from_value * 2.20462
# # elif conversion_number == 4:  # Pounds to Kilograms
# #     to_value = from_value / 2.20462
# # elif conversion_number == 5:  # Inches to Centimeters
# #     to_value = from_value * 2.54
# # elif conversion_number == 6:  # Centimeters to Inches
# #     to_value = from_value / 2.54
# # elif conversion_number == 7:  # Fahrenheit to Celsius
# #     to_value = (from_value - 32) * 5/9

# # # Display result
# # print(f"\n{from_value} {from_unit} -> {to_value:.2f} {to_unit}\n")
# import streamlit as st

# st.title("Unit Converter App")

# # Conversion options
# conversions_available = {
#     "Kilometers to Miles": lambda x: x * 0.621371,
#     "Miles to Kilometers": lambda x: x / 0.621371,
#     "Kilograms to Pounds": lambda x: x * 2.20462,
#     "Pounds to Kilograms": lambda x: x / 2.20462,
#     "Inches to Centimeters": lambda x: x * 2.54,
#     "Centimeters to Inches": lambda x: x / 2.54,
#     "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
# }

# # Dropdown to select conversion
# conversion_type = st.selectbox("Choose conversion type", list(conversions_available.keys()))

# # Input field for value
# from_value = st.number_input(f"Enter value in {conversion_type.split()[0]}:", min_value=0.0)

# # Perform conversion
# if st.button("Convert"):
#     to_value = conversions_available[conversion_type](from_value)
#     st.success(f"{from_value} {conversion_type.split()[0]} → {to_value:.2f} {conversion_type.split()[-1]}")
import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .big-font { font-size:25px !important; font-weight: bold; color: #FF5733; }
        .result { font-size:20px !important; font-weight: bold; color: #008000; }
        .select-box { font-size:18px !important; }
        .convert-btn { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="big-font">🔥 Unit Converter App 🔥</p>', unsafe_allow_html=True)

# Conversion options
conversions_available = {
    "Kilometers to Miles": lambda x: x * 0.621371,
    "Miles to Kilometers": lambda x: x / 0.621371,
    "Kilograms to Pounds": lambda x: x * 2.20462,
    "Pounds to Kilograms": lambda x: x / 2.20462,
    "Inches to Centimeters": lambda x: x * 2.54,
    "Centimeters to Inches": lambda x: x / 2.54,
    "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
}

# Dropdown to select conversion
conversion_type = st.selectbox("📌 Choose conversion type:", list(conversions_available.keys()))

# Input field for value
from_value = st.number_input(f"✏️ Enter value in {conversion_type.split()[0]}:", min_value=0.0)

# Perform conversion
if st.button("🔄 Convert", key="convert-btn"):
    to_value = conversions_available[conversion_type](from_value)
    st.markdown(f'<p class="result">✅ {from_value} {conversion_type.split()[0]} → {to_value:.2f} {conversion_type.split()[-1]}</p>', unsafe_allow_html=True)
