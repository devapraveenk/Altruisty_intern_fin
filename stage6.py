import streamlit as st
def stage_6():
    st.header("STAGE 6")
    st.write(" 1. Conduct a thorough search to ensure your idea is not already patented.")
    title = st.text_area('What did you understand from research ')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Consult with a legal expert to determine the intellectual property rights associated with your idea.")
        title = st.text_area('What consulltation did you do ?')
    if st.button("Completed task 2"):
        st.write(" 3. File for copyright protection for any original content, such as branding materials or software code.")
        title = st.text_area('')
    if st.button("Completed task 3"):
        st.write(" 4. Consider applying for a patent if your idea is innovative and meets the criteria for patent ability. ")
        title = st.text_area('What meets the criteria for patent ability in your project')
    if st.button("Completed task 4"):
        st.write(" 5. Prepare the necessary documentation and drawings for the patent application. ")
        option = st.selectbox(
            ' ?',
            ('yess', 'NO'))
        st.write('You selected:', option)
        if option=='YES':
            st.button("Submit")
    if st.button("Completed task 5"):
        st.write(" 6. Work with a patent attorney to draft and file the patent application. ")
        option = st.selectbox(
                    ' ?',
                    ('Yup', 'NO'))
        st.write('You selected:', option)
        if option=='YES':
            st.button("Submit")
    if st.button("Completed task 6"):
        st.write(" 7. Respond to any office actions or objections from patent examiners.")
        option = st.selectbox(
                            ' ?',
                            ('Responded..', 'Not yet'))
        st.write('You selected:', option)
        if option=='Responded..':
            st.button("proceed")
    if st.button("Completed task 7"):
        st.write(" 8. Monitor the progress of the patent application and address any issues that arise. ")
        title = st.text_area('Issues that arose for patent application')
    if st.button("Completed task 8"):
        st.write(" 9. Explore international patent protection if you plan to expand globally.")
        option = st.selectbox(
            ' ?',
            ('Explored', 'Not yet'))
        st.write('You selected:', option)
        if option=='Explored':
            st.button("next")
    if st.button("Completed task 9"):
        st.write(" 10. Once granted, enforce your patent rights against any infringement. ")
        option = st.selectbox(
                    ' Did you complete?',
                    ('Completed', 'Not yet'))
        st.write('You selected:', option)
        if option=='Completed':
                    st.button("continue")
    if st.button("Continue with task 7"):
        st.switch_page("stage7.py")



        