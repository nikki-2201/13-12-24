import streamlit as st
st.title("Gross Salary Calculation")
sal = st.number_input("Enter total salary :",min_value=0)
st.write("Note for less than 10k hra and da are 67% and 23% for between 10k and 20k it is 69% and 76% above 20k it is 73% and 89%")
if st.button("Calculate Gross"):
    if (sal < 10000):
        HRA = (sal * 67) / 100
        DA = (sal * 73) / 100
    elif (sal >= 10000 and sal <= 20000):
        HRA = (sal * 69) / 100
        DA = (sal * 76) / 100
    else:
        HRA = (sal * 73) / 100
        DA = (sal * 89) / 100
    gross = HRA + DA + sal
    st.info(f"Gross salary: {gross}")


