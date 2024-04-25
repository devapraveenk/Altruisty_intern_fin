import streamlit as st
def stage_12():
    st.header("STAGE 12")
    st.write(" 1. Develop a customer feedback survey to gather insights on customer satisfaction, preferences, and pain points.")
    option = st.selectbox(
        ' Did you develop a customer feedback survey to gather insights on customer satisfaction, preferences, and pain points ?',
        ('Developed.', 'Not yet'))
    st.write('You selected:', option)
    if option=='Developed.':
        st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Identify the target audience for the survey and select the appropriate distribution channels.")
        title = st.text_area('What is your target audience for the survey and select the appropriate distribution channels ?')
    if st.button("Completed task 2"):
        st.write(" 3. Administer the survey to customers through email, social media, or in-person interactions.")
        title = st.text_area('What process did you do for the survey to customers through email, social media, or in-person interactions ?')
    if st.button("Completed task 3"):
        st.write(" 4. Analyze the survey responses to identify trends and patterns in customer feedback. ")
        title = st.text_area('')
    if st.button("Completed task 4"):
        st.write(" 5. Segment the survey data based on demographics, usage behavior, or other relevant factors. ")
        title = st.text_area('What are segments of survey data based on demographics, usage behavior, or other relevant factors?')
    if st.button("Completed task 5"):
        st.write(" 6. Extract actionable insights from the survey findings to inform decision-making. ")
        title = st.text_area('What are the actionable insights from the survey findings to inform decision-making? ')
    if st.button("Completed task 6"):
        st.write(" 7. Share the survey results with key stakeholders, such as product teams and senior management.")
        title = st.text_area('')
    if st.button("Completed task 7"):
        st.write(" 8. Use customer feedback to prioritize product enhancements or service improvements. ")
        title = st.text_area('What was the feedback ?')
    if st.button("Completed task 8"):
        st.write(" 9. Implement changes based on customer input and communicate updates to customers. ")
        title = st.text_area('What changes did you do? ')
    if st.button("Completed task 9"):
        st.write(" 10. Follow up with customers to measure the impact of changes and gather additional feedback. ")
        title = st.text_area('List down the extra feedbacks ')
    st.button("Completed task 10")
    if st.button("Continue with task 13"):
        st.switch_page("stage13.py")



        