import streamlit as st
from converter import convert_length,convert_temperature,convert_currency,convert_speed,convert_time,convert_weight
st.title("Unit Converter")
f=open("list.txt","r")
l=f.readlines()
l=list(map(lambda x:x.strip(),l))
unit_type = st.selectbox("Select the Type of Unit",['Length','Temperature','Weight','Time','Speed','Currency'])
if unit_type=='Length':
    st.header('Length Coversion')
    val = st.number_input("Enter the value",min_value=0.0, value=1.0)
    f = st.selectbox("From",['centimeter','meter','inches','feet','Kilometer'])
    t=st.selectbox("To",['centimeter','meter','inches','feet','Kilometer'])
    if st.button("Convert"):
        result = convert_length(val,f,t)
        st.write(f"{val} {f} is equal to {result:.2f} {t}")
        
elif unit_type == "Temperature":
    st.header("Temperature Converter")
    value = st.number_input("Enter temperature:",min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value}° {from_unit} is equal to {result:.2f}° {to_unit}")
        
elif unit_type=="Weight":
    st.header("Weight Converter")
    value = st.number_input("Enter weight:",min_value=0.0, value=1.0)
    from_unit = st.selectbox("From", ["Gram", "Kilogram","Pound","Ounce"])
    to_unit = st.selectbox("To", ["Gram", "Kilogram","Pound","Ounce"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        

elif unit_type=="Speed":
    st.header("Speed Converter")
    value = st.number_input("Enter speed:",min_value=1.0, value=1.0)
    from_unit = st.selectbox("From", ["kph", "mps"])
    to_unit = st.selectbox("To",  ["kph", "mps"])
    if st.button("Convert"):
        result = convert_speed(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        
elif unit_type=="Time":
    st.header("Time Converter")
    value = st.number_input("Enter time:",min_value=0, value=1,step=1)
    from_unit = st.selectbox("From", ["Second", "Minute","Hour","Day"])
    to_unit = st.selectbox("To", ["Second", "Minute","Hour","Day"])
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        
elif unit_type=="Currency":
    st.header("Currency Converter")
    value = st.number_input("Enter weight:",min_value=1, value=1,step=1)
    from_unit = st.selectbox("From", l)
    to_unit = st.selectbox("To", l)
    if st.button("Convert"):
        result = convert_currency(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        


        
        
