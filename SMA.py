import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Name", "Maths", "Physics", "Chemistry", "IT", "Biology"])
if "name_entered" not in st.session_state:
    st.session_state["name_entered"] = False
st.title("Student Marks Analysis")
if not st.session_state["name_entered"]:
    with st.form("student_name_form", clear_on_submit=True):
        name = st.text_input("Enter Student Name")
        submit_name = st.form_submit_button("Next")
    
    if submit_name:
        st.session_state["name_entered"] = True
        st.session_state["name"] = name

# Second Step: Enter Student Marks (after name is entered)
if st.session_state["name_entered"]:
    with st.form("marks_form", clear_on_submit=True):
        st.header(f"Enter Marks for {st.session_state['name']}")
        maths = st.number_input("Maths Marks", min_value=0, max_value=100)
        physics = st.number_input("Physics Marks", min_value=0, max_value=100)
        chemistry = st.number_input("Chemistry Marks", min_value=0, max_value=100)
        it = st.number_input("IT Marks", min_value=0, max_value=100)
        biology = st.number_input("Biology Marks", min_value=0, max_value=100)
        submit_marks = st.form_submit_button("Add Student")
    
    if submit_marks:
        new_entry = {
            "Name": st.session_state["name"],
            "Maths": maths, "Physics": physics, "Chemistry": chemistry, 
            "IT": it, "Biology": biology
        }
        st.session_state["data"] = pd.concat([st.session_state["data"], pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Added data for {st.session_state['name']}!")
        st.session_state["name_entered"] = False  # Reset form for next student
# Display Data
st.header("Student Marks Table")
st.dataframe(st.session_state["data"])
# Analysis Section
if not st.session_state["data"].empty:
    st.header("Marks Analysis")
    for subject in ["Maths", "Physics", "Chemistry", "IT", "Biology"]:
        highest = st.session_state["data"].loc[st.session_state["data"][subject].idxmax()]
        lowest = st.session_state["data"].loc[st.session_state["data"][subject].idxmin()]
        st.write(f"**{subject}**")
        st.write(f"Highest Marks: {highest[subject]} by {highest['Name']}")
        st.write(f"Lowest Marks: {lowest[subject]} by {lowest['Name']}")
        st.markdown("---")
    # Graph for Comparison of All Students
    st.header("Marks Comparison - All Students")
    subjects = ["Maths", "Physics", "Chemistry", "IT", "Biology"]
    plt.figure(figsize=(10, 6))
    for student in st.session_state["data"]["Name"]:
        student_data = st.session_state["data"][st.session_state["data"]["Name"] == student]
        plt.plot(subjects, student_data.iloc[0, 1:], marker='o', label=student)
    plt.title("Comparison of Marks Across Students")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.legend(title="Students")
    plt.grid(True)
    st.pyplot(plt)