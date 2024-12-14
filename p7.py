import streamlit as st
st.title("Shopping bills")
sal = st.number_input("Enter salary: ",min_value=0)
st.write(f"Total salary",sal)
bill1 = st.number_input("first bill: ",min_value=0)
st.write("first bill",bill1)
bill2 = st.number_input("sec bill: ",min_value=0)
st.write("sec bill",bill2)
bill3 = st.number_input("third bill: ",min_value=0)
st.write("third bill",bill3)
total = bill1 + bill2 + bill3
if st.button("Calculate Total and percentage"):
    if (sal != 0):
        percentage = (total / sal) * 100
        st.success(f"Total Amount : {total}")
        st.success(f"percent spent on salary : {percentage:.2f}%")
    else:
        st.error("salary cannot be zero")


