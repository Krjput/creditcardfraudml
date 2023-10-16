import streamlit as st

st.title("Credit Card Fraud Detection")

st.info("Please fill the following details to predict wheather the transaction is fraud or not")

cc_number = st.text_input("Enter your credit card number")

amnt = st.number_input("Enter the amount of transaction")

gender = st.text_input("Enter Your Gender Male(1) Female(0)")

zipcode = st.text_input("Enter your zipcode")

lat = st.text_input("Enter your latitude")

long = st.text_input("Enter your longitude")

city_pop = st.text_input("Enter your city population")

unix_time = st.text_input("Enter your unix time")

merch_lat = st.text_input("Enter your merchant latitude")

merch_long = st.text_input("Enter your merchant longitude")

def creditcard():
    # Check if all input fields are filled
    if not all([cc_number, amnt,gender, zipcode, lat,long,city_pop,unix_time,merch_lat,merch_long]):    
        st.warning("Please fill in all the features.")
    else:
       if amnt%2 == 0:
        st.error(" Transcation is fraud")
       else:
        amnt%2 != 0
        st.success("Transcation is not fraud")


# Create a button to trigger the car price prediction
if st.button("Predict The Transcation"):
    creditcard()

# Footer
st.markdown("---")
st.write("Designed and Developed by Kanishka Rajput")
