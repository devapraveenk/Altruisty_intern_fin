import streamlit as st
def stage_2():
    st.header("STAGE 2")
    st.write(" 1. Develop a minimum viable product (MVP) to demonstrate the core functionality.")
    title = st.text_input('1. Identify and point out your assumptions', '')
    title = st.text_input('2. Identify minimum features needed to start your project', '')
    title = st.text_input('3. Build MVP and test your hypothesis', '')
    st.link_button("How to develop MVP ?", "https://uizard.io/blog/how-to-create-a-succesful-mvp-a-step-by-step-guide/")
    st.button("submit")
    if st.button("Completed task 1"):

        st.write(" 2. Test the MVP with a small group of users or beta testers.")
    option = st.selectbox(
        'Did you complete testing wih small group?',
        ('YES', 'NO'))
    st.write('You selected:', option)
    if option=='YES':
        st.button("Submit")
    if st.button("Completed task 2"):
        st.write(" 3. Gather feedback on the usability and performance of the POC.")
        md = st.text_area('give the feedback')
        st.link_button("To know more about templates...","https://slideuplift.com/blog/best-websites-for-powerpoint-templates/")
    if st.button("Completed task 3"):
        st.write(" 4. Iterate on the POC based on user feedback. ")
        d = st.text_area(' What was the repeated feedback ?')
    if st.button("Completed task 4"):
        st.write(" 5. Measure key metrics to validate the effectiveness of the concept.")
        md = st.text_area('What are the key metrics to validate your concept?')
    if st.button("Completed task 5"):

        st.write(" 6. Identify any technical or operational challenges.")
        md = st.text_area('What challenges did you find difficult ?')
    if st.button("Completed task 6"):
        st.write(" 7. Refine the POC to address any identified issues.")
        option = st.selectbox(
        'Did you refine the issues ?',
        ('YES', 'NO'))
        st.write('You selected:', option)
        if option=='YES':
            st.button("next")
    if st.button("Completed task 7"):
        st.write(" 8. Document the POC process and outcomes for future reference. ")
        option = st.selectbox(
            'Did you prepare your document ?',
            ('Prepared', 'Not yet'))
        st.write('You selected:', option)       
    if option=='Prepared':
        st.button("proceed")
    if st.button("Completed task 8"):

        st.write(" 9. Assess the scalability of the concept. ")
        b = st.text_area('List down your concept')
    if st.button("Completed task 9"):
        st.write(" 10. Analyze the cost-effectiveness of scaling the POC. ")
        title = st.text_input('Did you analyse the cost-effectiveness ?', '')
        st.button("Completed task 10")
    if st.button("Continue with task 3"):
        st.switch_page("stage3.py")



        