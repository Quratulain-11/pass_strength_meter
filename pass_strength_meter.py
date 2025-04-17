import streamlit as st
import re

st.set_page_config(page_title="Password strength character",page_icon='💡')

st.title('password strength checker ')
st.markdown("""
            ## Welcome to the ultimate password strength checker!
           use this simple tool to check the strengthof yuor password and get suggestions on how to make it stronger.
                    we will give you helpfull tips to create a **Strong Password**  """)

password = st.text_input("Enter your password", type='password')

feedback = []

score = 0 
if password:
    if len(password) >= 8:
        score += 1
    else : 
        feedback.append("password should be atleast 8 characters long.")

    if re.search (r'[A-Z]', password) and re.search (r'[a-z]',password):
         score += 1
    
    else:
        feedback.append("passowrd should control both upper and lower case character.")

    if re.search(r'\d',password):
        score += 1 

    else :
        feedback.append("password should contain atleast one digit.")

    if re.search(r'[!@#$%&*]',password):
        score += 1

    else :
        feedback.append("password should contain one special character!(!@#$%&*)")            

    if score == 4:
        feedback.append("your password is strong!")
    elif score == 3 :
        feedback.append("your password is medium strength.It could be strong!")
    else:
        feedback.append("your password is weak please make it stonger") 


    if feedback:
        st.markdown(" ## Here's some suggestions for you!")
        for tip in feedback:
            st.write(tip)

else :
    st.info("Please enter your password to get started")            