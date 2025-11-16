import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="EV Range Prediction", layout="centered")

# Load dataset, model, scaler

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # go to Final_Project
csv_path = os.path.join(BASE_DIR, "electric_vehicles_spec.csv")
data = pd.read_csv(csv_path)

model_path = os.path.join(BASE_DIR, "model.pkl")
model = pickle.load(open(model_path, "rb"))

scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
scaler = pickle.load(open(scaler_path, "rb"))


st.markdown("<h2 style='text-align:center;'>EV Range Prediction</h2>", unsafe_allow_html=True)
st.write("### Please input details of your EV:")

# Convert to string for dropdowns
data["brand"] = data["brand"].astype(str)
data["model"] = data["model"].astype(str)
data["battery_type"] = data["battery_type"].astype(str)

# --------------------------- DROPDOWNS ---------------------------
st.markdown("**Brand (Encoded number) — Allowed: 0 to 11**")
brand_str = st.selectbox("Select Car Brand", sorted(data["brand"].unique()))

st.markdown("**Model (Encoded number) — Allowed: 0 to 212**")
model_str = st.selectbox("Select Car Model", sorted(data["model"].unique()))

st.markdown("**Battery Type (Encoded number) — Allowed: 0 or 1**")
battery_str = st.selectbox("Select Battery Type", sorted(data["battery_type"].unique()))

def safe_convert(x):
    try:
        return int(x)
    except:
        return 0

brand_val = safe_convert(brand_str)
model_val = safe_convert(model_str)
battery_val = safe_convert(battery_str)

# --------------------------- TEXT INPUTS ---------------------------
st.markdown("**Top Speed (km/h) — 150 to 300**")
top_speed = st.text_input("Enter Top Speed (km/h)")

st.markdown("**Battery Capacity (kWh) — 35 to 90**")
battery_capacity = st.text_input("Enter Battery Capacity (kWh)")

st.markdown("**Number of Cells — 100 to 400**")
num_cells = st.text_input("Enter Number of Cells")

st.markdown("**Torque (Nm) — 200 to 1000**")
torque = st.text_input("Enter Torque (Nm)")

st.markdown("**Acceleration (0–100s) — 3 to 10**")
accel = st.text_input("Enter Acceleration 0–100 (s)")

st.markdown("**Fast Charging Power (kW DC) — 50 to 120**")
fast_charge = st.text_input("Enter Fast Charging Power (kW DC)")

# --------------------------- PREDICTION ---------------------------
if st.button("Predict"):
    try:
        df = pd.DataFrame([[
            brand_val, model_val, float(top_speed), float(battery_capacity),
            battery_val, float(num_cells), float(torque),
            float(accel), float(fast_charge)
        ]], columns=[
            'brand', 'model', 'top_speed_kmh', 'battery_capacity_kWh',
            'battery_type', 'number_of_cells', 'torque_nm',
            'acceleration_0_100_s', 'fast_charging_power_kw_dc'
        ])

        scaled = scaler.transform(df)
        pred = model.predict(scaled)

        st.success(f"Predicted EV Range: {pred[0]:.2f} km")

        # -------------- GRAPHS IN TABS --------------
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["📊 Bar Graph", "🥧 Pie Chart", "📈 Line Chart", "🔵 Scatter Plot", "🔋 Battery Diagram"]
        )

        with tab1:
            st.subheader("Predicted Range (Bar Graph)")
            fig1, ax1 = plt.subplots()
            ax1.bar(["Predicted Range"], [pred[0]], color="blue")
            ax1.set_ylabel("Range (km)")
            st.pyplot(fig1)

        with tab2:
            st.subheader("Battery vs Range (Pie Chart)")
            sizes = [float(battery_capacity), pred[0]]
            labels = ["Battery Capacity", "Predicted Range"]
            fig2, ax2 = plt.subplots()
            ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
            st.pyplot(fig2)

        with tab3:
            st.subheader("Torque vs Range (Line Chart)")
            fig3, ax3 = plt.subplots()
            ax3.plot([float(torque)], [pred[0]], marker="o")
            ax3.set_xlabel("Torque (Nm)")
            ax3.set_ylabel("Range (km)")
            st.pyplot(fig3)

        with tab4:
            st.subheader("Battery Capacity vs Range (Scatter Plot)")
            fig4 = px.scatter(
                x=[float(battery_capacity)],
                y=[pred[0]],
                labels={"x": "Battery Capacity (kWh)", "y": "Predicted Range (km)"},
                title="Battery Capacity vs Range"
            )
            st.plotly_chart(fig4)

        with tab5:
            st.subheader("EV Battery Diagram")
            st.image("battery_diagram.png", caption="Battery Diagram", use_column_width=True)

    except Exception as e:
        st.error(f"⚠ Error: {e}")


