import streamlit as st

st.title("Hotel Booking Cancellation Prediction")

lead_time = st.number_input("Lead Time", 0, 500)
adr = st.number_input("ADR", 0.0, 500.0)

if st.button("Predict"):
    if lead_time > 50 and adr > 100:
        st.error("High chance of cancellation")
    else:
        st.success("Low chance of cancellation")
