import streamlit as st

st.set_page_config(page_title="About EV Prediction App", layout="centered")


st.markdown("<h2 style='text-align:center;'>About This Project</h2>", unsafe_allow_html=True)

st.write("")
st.write(
    """
This web application is designed to **predict the driving range of Electric Vehicles (EVs)**  
based on key technical specifications such as top speed, battery capacity, number of cells,  
torque, acceleration, and fast charging power.

The goal of this project is to:
- Help users **estimate expected EV range** before purchasing.
- Provide a **simple and user-friendly interface** to understand EV performance.
- Demonstrate how **Machine Learning models** can be applied in the automobile industry.
"""
)

st.write("---")


st.markdown("### 🔧 How the Model Works")
st.write(
    """
- The application uses a **Linear Regression ML model**.  
- Input values are **scaled using StandardScaler** to maintain accuracy.  
- The model was trained on a dataset of **various electric vehicle specifications**.  
- Based on the inputs, it predicts the **expected EV range (in km)**.
"""
)

st.write("---")


st.markdown("### ⚡ Why EV Range Prediction Matters")
st.write(
    """
Predicting EV range helps users understand:
- Expected performance on full charge  
- Whether a vehicle is suitable for long-distance travel  
- Charging needs and efficiency  
- Comparison between different EV models  
"""
)

st.write("---")


st.markdown("### 📊 Dataset Information")
st.write(
    """
The dataset includes:
- Multiple EV Brands and Models  
- Technical specs like battery type, motor power, acceleration, torque, etc.  
- Real-world EV performance indicators  
"""
)

st.write("---")


st.markdown("### 👩‍💻 Developer")
st.write(
    """
This EV Range Prediction App was developed by **Sonali Jha**  
as part of an ML + Streamlit hands-on learning project.
"""
)

st.write("---")

st.markdown(
    "<p style='text-align:center; font-size:14px; color:gray;'>Thank you for using the EV Prediction App ⚡</p>",
    unsafe_allow_html=True
)

