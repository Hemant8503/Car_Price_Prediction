import streamlit as st
import pandas as pd
import pickle

# Load the trained model

model = pickle.load(open("C:\\Users\\hp\\Desktop\\car_price\\updated_model_CP.pkl" , 'rb'))
df = pd.read_csv("car data.csv")


# Define the user input interface
st.title("Car Price Prediction")
st.write("Enter the car details below:")

# User inputs
unique_values = df["Car_Name"].unique().tolist()
car_name = st.selectbox("Select Car Name : ", unique_values)
present_price = st.number_input("Present Price (Lakhs)", value=0)
kms_driven = st.number_input("Kilometers Driven (km)", value=0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

# Calculate the car's age based on the user input year
years = st.number_input('In which year car was purchased ?',1990, 2023, step=1, key ='year')
years_old = 2022-years



# Display the prediction to the user
if st.button("Estimate Price", key='predict'):
    # Make the prediction
    prediction = model.predict(pd.DataFrame([[car_name,present_price, kms_driven,fuel_type,seller_type,transmission, owner, years_old]],columns=['Car_Name','Present_Price' ,	'Kms_Driven' ,	'Fuel_Type' ,	'Seller_Type' ,	'Transmission' ,	'Owner' ,	'Years_old']))
    output = round(prediction[0],2)
    if output<0:
        st.warning("You will be not able to sell this car !!")
    else:
        st.success("You can sell the car for {} lakhs 🙌".format(output))    
    
    
   
    


# pipe.predict(pd.DataFrame([['ritz',5.59 , 27000 ,'Petrol','Dealer','Manual',0,9]],columns=['Car_Name',	'Present_Price' ,	'Kms_Driven' ,	'Fuel_Type' ,	'Seller_Type' ,	'Transmission' ,	'Owner' ,	'Years_old']))

