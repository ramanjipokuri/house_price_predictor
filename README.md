# 🏠 House Price Prediction Web App

This project is an **end-to-end Machine Learning solution** that predicts the price of residential homes based on input features such as bedrooms, bathrooms, square footage, grade, and location.  
The model is deployed as a fully interactive **Streamlit web application**, allowing real-time predictions through a user-friendly interface.

---

## 🔗 Live Application

👉 Try the deployed app here:  
**Streamlit Deploy Link :- <https://housepricepredictor-ze2kz9pmyddjazrprdn3aq.streamlit.app/>**

---

## 🚀 Project Overview

This project follows a complete Data Science & MLOps workflow:

| Phase | Description |
|-------|------------|
| ✔ Data Collection | Imported housing dataset (King County, USA) |
| ✔ Data Cleaning | Handled datatypes, removed unused columns, fixed formatting |
| ✔ Exploratory Data Analysis (EDA) | Correlation heatmaps, distribution plots, boxplots |
| ✔ Feature Engineering | Selected relevant numeric features |
| ✔ Model Training | Used Random Forest Regressor |
| ✔ Model Evaluation | Achieved strong score (R² ≈ **0.85**) |
| ✔ Model Saving | Serialized using `joblib` |
| ✔ Deployment | Hosted with Streamlit Cloud |

---

## 📊 Dataset Information

- **Rows:** ~21,600
- **Columns:** 21
- **Target Variable:** `price`

Key features include:

- Bedrooms, bathrooms
- Living & lot square footage
- Waterfront, view, condition, grade
- Geographic coordinates (lat/long)
- Year built & renovated

---

## 🧠 Model Performance

| Metric | Value |
|--------|-------|
| RMSE | ~148,000 |
| R² Score | ~0.85 |

The Random Forest model performed well, balancing accuracy and generalization.

---

## 🧰 Technologies Used

| Category | Tools |
|---------|-------|
| Programming | Python |
| ML Libraries | Scikit-Learn, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit Cloud |
| Serialization | Joblib |
| Version Control | Git + GitHub |

---

## 📦 Installation (Run Locally)    

Clone the repo:

```bash
git clone (https://github.com/ramanjipokuri/house_price_predictor/blob/main/app.py)
