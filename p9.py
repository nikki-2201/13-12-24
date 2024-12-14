import streamlit as st
st.title("Grades")
project = st.number_input("Enter project score: ",min_value=0,max_value=100)
internal = st.number_input("Enter internal score: ",min_value=0,max_value=100)
external = st.number_input("Enter external score: ",min_value=0,max_value=100)
if st.button("Get Grade"):
    if project >= 50 and internal >= 50 and external >= 50:
        total = (project * 0.70) + (internal * 0.10) + (external * 0.20)
        st.write(f"Total marks : ",total)
        if (total > 90):
            st.success("A grade")
        elif (total > 80 and total <= 90):
            st.success("B grade")
        else:
            st.success("C grade")

    if (project < 50):
        st.error(f"Failed in project and secured marks: {project}")
    if (internal < 50):
        st.error(f"Failed in internal and secured marks: {internal}")
    if (external < 50):
        st.error(f"Failed in external and secured marks: {external}")

