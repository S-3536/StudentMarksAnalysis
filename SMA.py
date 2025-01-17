import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
subjects = ["Maths","Physics","Chemistry","Biology","English","IT"]
st.title("Student Marks Analysis")
num_students=st.number_input("Enter the number of students",min_value=1,step=1)
if num_students>0:
    data={
        "S.No.":list(range(1,int(num_students)+1)),
        "Name":[f"Student {i+1}" for i in range(int(num_students))]
    }
    for subject in subjects:
        data[subject]=[0.0]*int(num_students)
    student_data=pd.DataFrame(data)
    st.subheader("Enter student names and marks:")
    edited_data=st.data_editor(student_data,num_rows="dynamic",disabled=["S.No."])
    if not edited_data["Name"].isnull().any():
        edited_data["Average Marks"]=edited_data[subjects].mean(axis=1)
        st.subheader("Student marks table")
        st.dataframe(edited_data)
        st.subheader("Highest and lowest marks in each subject")
        for subject in subjects:
            highest_mark=edited_data[subject].max()
            lowest_mark=edited_data[subject].min()
            highest_student=edited_data.loc[edited_data[subject]==highest_mark,"Name"].values[0]
            lowest_student=edited_data.loc[edited_data[subject]==lowest_mark,"Name"].values[0]
            st.write(f"{subject}:Highest ={highest_mark} by {highest_student},lowest={lowest_mark} by {lowest_student}")
        st.subheader("Graph for student marks")
        fig,ax=plt.subplots(figsize=(10,6))
        for _, row in edited_data.iterrows():
            ax.plot(subjects,row[subjects],marker='o',label=row["Name"])
        ax.set_title("Student marks in each subject")
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Marks")
        ax.legend(title="Students")
        st.pyplot(fig) 
    else:
        
        st.warning("Please enter all student names.")          
