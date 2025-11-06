import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))


st.header('Car Efficiency Prediction ML Model')

cars_data = pd.read_csv('electric_vehicles_spec_2025.csv.csv')

brand= cars_data['brand'].unique()

brand_mapping = {brand: i for i, brand in enumerate(cars_data['brand'].unique())}


brand = st.selectbox('Select Car Brand', list(brand_mapping.keys()))
brand_encoded = brand_mapping[brand]

top_speed_kmh = st.slider("Car Top Speed (km/h)", 120, 350)
battery_capacity_kWh = st.slider("Battery Capacity (kWh)", 20, 150)
range_km = st.slider("Range (km)", 100, 800)
acceleration_0_100_s = st.slider("Acceleration 0-100 km/h (s)", 2.0, 15.0)
fast_charging_power_kw_dc = st.number_input("Fast Charging Power (kW DC)")

seats = st.slider("Number of seats", 2, 7)

car_body_mapping = {
'Hatchback': 1,
 'SUV': 2,
 'Station/Estate': 3,
 'Liftback Sedan': 4,
 'Sedan': 5,
 'Small Passenger Van': 6,
 'Cabriolet': 7,
 'Coupe': 8}

car_body_type = st.selectbox("Select Car Body type",['Hatchback','SUV','Station/Estate','Liftback Sedan','Sedan','Small Passenger Van','Cabriolet','Coupe'])
car_body_type_encoded = car_body_mapping[car_body_type]



if st.button("Predict"):

    input_data_model = pd.DataFrame([[
        brand_encoded, top_speed_kmh, battery_capacity_kWh, range_km,acceleration_0_100_s, fast_charging_power_kw_dc, seats, car_body_type_encoded
    ]], columns=[
        'brand', 'top_speed_kmh', 'battery_capacity_kWh', 'range_km',
        'acceleration_0_100_s', 'fast_charging_power_kw_dc', 'seats', 'car_body_type'
    ])

    car_efficiency = model.predict(input_data_model)
    st.markdown('The efficiency of the Car is: '+str(car_efficiency[0]))