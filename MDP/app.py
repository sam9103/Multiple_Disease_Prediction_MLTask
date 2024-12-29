import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Disease mapping
disease_mapping = {
    0: "Anemia",
    1: "Diabetes",
    2: "Healthy",
    3: "Heart Disease",
    4: "Thalassemia",
    5: "Thrombocytopenia"
}


st.title("Multiple Disease Prediction App")
st.markdown("### Enter the following details:")

# Input fields for the 24 features
glucose = st.number_input("Glucose (mg/dL)", step=0.1, format="%.2f")
cholesterol = st.number_input("Cholesterol (mg/dL)", step=0.1, format="%.2f")
hemoglobin = st.number_input("Hemoglobin (g/dL)", step=0.1, format="%.2f")
platelets = st.number_input("Platelets (x10^3/uL)", step=0.1, format="%.2f")
white_blood_cells = st.number_input("White Blood Cells (cells/uL)", step=0.1, format="%.2f")
red_blood_cells = st.number_input("Red Blood Cells (million cells/mcL)", step=0.1, format="%.2f")
hematocrit = st.number_input("Hematocrit (%)", step=0.1, format="%.2f")
mean_corpuscular_volume = st.number_input("Mean Corpuscular Volume (fL)", step=0.1, format="%.2f")
mean_corpuscular_hemoglobin = st.number_input("Mean Corpuscular Hemoglobin (pg)", step=0.1, format="%.2f")
mean_corpuscular_hemoglobin_concentration = st.number_input("Mean Corpuscular Hemoglobin Concentration (g/dL)", step=0.1, format="%.2f")
insulin = st.number_input("Insulin (mU/L)", step=0.1, format="%.2f")
bmi = st.number_input("BMI (kg/m²)", step=0.1, format="%.2f")
systolic_blood_pressure = st.number_input("Systolic Blood Pressure (mmHg)", step=0.1, format="%.2f")
diastolic_blood_pressure = st.number_input("Diastolic Blood Pressure (mmHg)", step=0.1, format="%.2f")
triglycerides = st.number_input("Triglycerides (mg/dL)", step=0.1, format="%.2f")
hba1c = st.number_input("HbA1c (%)", step=0.1, format="%.2f")
ldl_cholesterol = st.number_input("LDL Cholesterol (mg/dL)", step=0.1, format="%.2f")
hdl_cholesterol = st.number_input("HDL Cholesterol (mg/dL)", step=0.1, format="%.2f")
alt = st.number_input("ALT (U/L)", step=0.1, format="%.2f")
ast = st.number_input("AST (U/L)", step=0.1, format="%.2f")
heart_rate = st.number_input("Heart Rate (bpm)", step=0.1, format="%.2f")
creatinine = st.number_input("Creatinine (mg/dL)", step=0.1, format="%.2f")
troponin = st.number_input("Troponin (ng/mL)", step=0.1, format="%.2f")
c_reactive_protein = st.number_input("C-reactive Protein (mg/L)", step=0.1, format="%.2f")


if st.button("Predict"):
    try:
        # List of all inputs
        features = [
            glucose, cholesterol, hemoglobin, platelets, white_blood_cells,
            red_blood_cells, hematocrit, mean_corpuscular_volume,
            mean_corpuscular_hemoglobin, mean_corpuscular_hemoglobin_concentration,
            insulin, bmi, systolic_blood_pressure, diastolic_blood_pressure,
            triglycerides, hba1c, ldl_cholesterol, hdl_cholesterol,
            alt, ast, heart_rate, creatinine, troponin, c_reactive_protein
        ]

       
        if any(value is None or value == "" for value in features):
            st.error("Please fill out all fields before predicting.")
        else:
           
            test_data = np.array(features).reshape(1, -1)

            # Predict the disease
            prediction = model.predict(test_data)[0]
            result = disease_mapping.get(prediction, "Unknown Disease")

            # Display the result
            st.success(f"The predicted disease is: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
