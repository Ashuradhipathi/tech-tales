import streamlit as st 
import requests
import pymongo
from twilio.rest import Client as cl

#account_sid = st.secrets["account_sid"]
#auth_token = st.secrets["auth_token"]
#twilio_phone_number = st.secrets["twilio_phone_number"]
#client1 = cl(account_sid, auth_token)
#client = pymongo.MongoClient(st.secrets["mclient"])
#db = client["Tech_Tales"]
#collection = db["comments"]
def main():
    st.markdown("""
    <div style='text-align: center;'>
        <h2>Tech-Tales</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(" Ever wondered about the person behind the code? With TechTales, you can now access personal information such as names, emails, and bios of GitHub users, shared willingly by them in the spirit of openness and connection.")
if __name__ == "__main__":
    main()
