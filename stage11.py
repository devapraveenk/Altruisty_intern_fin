import streamlit as st
def stage_11():
    st.header("STAGE 11")
    st.write(" 1. Develop a detailed implementation plan outlining the steps and resources required to launch your startup.")
    title = st.text_area('Give the detailed implementation plan')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Allocate roles and responsibilities to team members for executing the implementation plan.")
        title = st.text_area('What roles did you allocate to the team members')
    if st.button("Completed task 2"):
        st.write(" 3. Secure the necessary infrastructure, equipment, and technology to support your operations.")
        title = st.text_area('What process did you try to secure youur operations ?')
    if st.button("Completed task 3"):
        st.write(" 4. Establish partnerships with suppliers, vendors, and service providers. ")
        title = st.text_area('List down the suppliers, vendors, and service providers')
    if st.button("Completed task 4"):
        st.write(" 5. Conduct a soft launch or pilot test to validate your product or service in a controlled environment. ")
        option = st.selectbox(
            ' Did you conduct ?',
            ('Conducted.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Conducted.':
            st.button("next")
    if st.button("Completed task 5"):
        st.write(" 6. Monitor key performance indicators (KPIs) to track the progress of your implementation efforts. ")
        title = st.text_area('How is your progress ?')
    if st.button("Completed task 6"):
        st.write(" 7. Address any operational challenges or issues that arise during the implementation phase.")
        title = st.text_area('What are the operational challenges or issues that you phased during the implementation phase ?')
    if st.button("Completed task 7"):
        st.write(" 8. Train employees on new processes, systems, and procedures. ")
        title = st.text_area('What new process did you train your employees ?')
    if st.button("Completed task 8"):
        st.write(" 9. Implement feedback mechanisms to gather input from customers and stakeholders. ")
        title = st.text_area('What feedback did you get ?')
    if st.button("Completed task 9"):
        st.write(" 10. Continuously iterate and improve your implementation approach based on lessons learned. ")
        title = st.text_area('What new changes did you make?')
    st.button("Completed task 10")
    if st.button("Continue with task 12"):
        st.switch_page("stage12.py")



        