import streamlit as st
def stage_7():
    st.header("STAGE 7")
    st.write(" 1. Translate the finalized prototype design into a functional prototype.")
    title = st.text_area('Did you start the process and how ?')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Select the appropriate technologies and tools for prototype development.")
        title = st.text_area('What tool did you use')
    if st.button("Completed task 2"):
        st.write(" 3. Divide the development process into manageable tasks and set milestones.")
        title = st.text_area('List out the divided tasks')
    if st.button("Completed task 3"):
        st.write(" 4. Build the back end infrastructure to support the prototype. ")
        title = st.text_area('How are you going to procced with backend?')
    if st.button("Completed task 4"):
        st.write(" 5. Develop the front end interface according to the design specifications. ")
        title = st.text_area('Contact frontend team and list their suggestions')
    if st.button("Completed task 5"):
        st.write(" 6. Test each component of the prototype for functionality and performance. ")
        option = st.selectbox(
            ' ?',
            ('Tested', 'Not yet'))
        st.write('You selected:', option)
        if option=='Tested':
            st.button("next")
    if st.button("Completed task 6"):
        st.write(" 7. Integrate feedback from users and stakeholders during the development process.")

        option = st.selectbox(
        ' ?',
        ('Completed.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Completed.':
            st.button("next")
    if st.button("Completed task 7"):
        st.write(" 8. Debug and optimize the prototype for speed, reliability, and scalability. ")
        title = st.text_area('How are you going to start with debugging process and list them out')
    if st.button("Completed task 8"):
        st.write(" 9. Conduct thorough QA testing to identify and fix any bugs or issues. ")
        option = st.selectbox(
            ' ?',
            ('Conducted', 'Not yet'))
        st.write('You selected:', option)
        if option=='Conducted':
            st.button("next")
    if st.button("Completed task 9"):
        st.write(" 10. Document the development process and any technical challenges encountered. ")
        title = st.text_area('Write the documentation part in here')
    st.button("Completed task 10")
    if st.button("Continue with task 8"):
        st.switch_page("stage8.py")



        