
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
