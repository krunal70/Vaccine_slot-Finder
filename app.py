import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import requests as r



st.title("Vaccine Slot Notifier")

pincode=st.text_input("Enter your Area Pincode","")
date=st.text_input("Enter the date","")

url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin/?pincode={pincode}&date={date}"
x=r.get(url)

res=x.json()

if st.button("Submit"):
    i=1
    for slots in res["sessions"]:
        st.success(i)
        st.text("Name: ")
        st.success(slots["name"])
        st.text("Address: ")
        st.success(slots["address"])
        st.text("State_name: ")
        st.success(slots["state_name"])
        st.text("District: ")
        st.success(slots["district_name"])
        st.text("Block_name: ")
        st.success(slots["block_name"])
        st.text("Pincode: ")
        st.success(slots["pincode"])
        st.text("From: ")
        st.success(slots["from"])
        st.text("To: ")
        st.success(slots["to"])
        st.text("Fee_type: ")
        st.success(slots["fee_type"])
        st.text("Date: ")
        st.success(slots["date"])
        st.text("Available_capacity: ")
        st.success(slots["available_capacity"])
        st.text("Available_capacity for Dose-1: ")
        st.success(slots["available_capacity_dose1"])
        st.text("Available_capacity for Dose-2: ")
        st.success(slots["available_capacity_dose2"])
        st.text("Fee: ")
        st.success(slots["fee"])
        st.text("Min_age_limit: ")
        st.success(slots["min_age_limit"])
        st.text("Vaccine: ")
        st.success(slots["vaccine"])
        st.text("slots: ")
        st.success(slots["slots"])
        i=i+1

st.header("Made with ❤ by Krunal Dubey")

