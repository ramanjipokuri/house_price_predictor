import streamlit as st
import pandas as pd
import joblib

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    model = joblib.load("house_price_model.pkl")
    return model

model = load_model()

# ---------- APP TITLE & DESCRIPTION ----------
st.title("🏠 House Price Prediction App")
st.markdown("""
Welcome to the **House Price Prediction** tool.  

Enter house details in the sidebar, and the app will estimate the **price** based on a machine learning model trained on historical data.
""")

st.sidebar.header("🔧 Input House Details")

# ---------- SIDEBAR INPUTS ----------
bedrooms = st.sidebar.slider("Bedrooms", 0, 10, 3)
bathrooms = st.sidebar.slider("Bathrooms", 0.0, 5.0, 2.0, step=0.25)
sqft_living = st.sidebar.number_input("Living Area (sqft)", 200, 10000, 1800)
sqft_lot = st.sidebar.number_input("Lot Size (sqft)", 500, 1000000, 5000)
floors = st.sidebar.slider("Floors", 1.0, 4.0, 1.0, step=0.5)
waterfront = st.sidebar.selectbox("Waterfront", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
view = st.sidebar.slider("View (0–4)", 0, 4, 0)
condition = st.sidebar.slider("Condition (1–5)", 1, 5, 3)
grade = st.sidebar.slider("Grade (1–13)", 1, 13, 7)
sqft_above = st.sidebar.number_input("Sqft Above Ground", 200, 10000, 1500)
sqft_basement = st.sidebar.number_input("Sqft Basement", 0, 5000, 0)

yr_built = st.sidebar.number_input("Year Built", 1900, 2025, 1990)
yr_renovated = st.sidebar.number_input("Year Renovated (0 if never)", 0, 2025, 0)

# 🔥 NEW FIELD (required because model expects it)
zipcode = st.sidebar.number_input("Zipcode", min_value=98000, max_value=99999, value=98103)

lat = st.sidebar.number_input("Latitude", 47.0, 48.0, 47.5)
long = st.sidebar.number_input("Longitude", -123.0, -121.0, -122.2)
sqft_living15 = st.sidebar.number_input("Living Area (15 neighbors)", 200, 10000, 1800)
sqft_lot15 = st.sidebar.number_input("Lot Size (15 neighbors)", 500, 1000000, 5000)

# ---------- INPUT DATAFRAME ----------
input_data = pd.DataFrame({
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "sqft_living": [sqft_living],
    "sqft_lot": [sqft_lot],
    "floors": [floors],
    "waterfront": [waterfront],
    "view": [view],
    "condition": [condition],
    "grade": [grade],
    "sqft_above": [sqft_above],
    "sqft_basement": [sqft_basement],
    "yr_built": [yr_built],
    "yr_renovated": [yr_renovated],
    "zipcode": [zipcode],   # 🔥 ADDED HERE
    "lat": [lat],
    "long": [long],
    "sqft_living15": [sqft_living15],
    "sqft_lot15": [sqft_lot15]
})


st.subheader("📋 Your Input Summary")
st.write(input_data)

# ---------- PREDICTION BUTTON ----------
if st.button("🔮 Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: **${prediction:,.0f}**")
    st.caption("Note: This is an estimate based on historical data and may not reflect current market conditions.")
