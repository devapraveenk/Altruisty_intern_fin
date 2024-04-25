import streamlit as st
def stage_10():
    st.header("STAGE 10")
    st.write(" 1. Choose a suitable legal structure for your startup, such as a sole proprietorship, partnership, LLC, or corporation.")
    title = st.text_area('Write down the legal structure one by one')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Register your business name with the appropriate government authorities.")
        option = st.selectbox(
            ' Did you register?',
            ('Registered', 'Not yet'))
        st.write('You selected:', option)
        if option=='Registered':
            st.button("next")
    if st.button("Completed task 2"):
        st.write(" 3. Obtain any necessary business licenses or permits required for your industry.")
        option = st.selectbox(
            ' Did you obtain necessary permits ?',
            ('Obatined', 'Not yet'))
        st.write('You selected:', option)
        if option=='Obtained':
            st.button("next")
    if st.button("Completed task 3"):
        st.write(" 4. Register for taxes and obtain an employer identification number (EIN) if hiring employees. ")
        option = st.selectbox(
            ' Registered for taxes ?',
            ('Registered.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Registered.':
            st.button("next")
    if st.button("Completed task 4"):
        st.write(" 5. Open a business bank account to separate your personal and business finances. ")
        option = st.selectbox(
            ' Did you open business account ?',
            ('opened.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Opened.':
            st.button("next")
    if st.button("Completed task 5"):
        st.write(" 6. Draft and file the articles of incorporation or organization with the state. ")
        option = st.selectbox(
            ' Did you draft and file articles ?',
            ('Drafted.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Drafted.':
            st.button("next")
    if st.button("Completed task 6"):
        st.write(" 7. Determine the jurisdiction for incorporating your company based on tax and regulatory considerations.")
        title = st.text_area('What did you determine ?')
    if st.button("Completed task 7"):
        st.write(" 8. Consult with a legal advisor to ensure compliance with local regulations and requirements. ")
        title = st.text_area('What was the advice ?')
    if st.button("Completed task 8"):
        st.write(" 9. Establish corporate governance policies and procedures, such as bylaws and operating agreements. ")
        option = st.selectbox(
            ' Did you establish ?',
            ('Established.', 'Not yet'))
        st.write('You selected:', option)
        if option=='Established.':
            st.button("next")
    if st.button("Completed task 9"):
        st.write(" 10. Obtain any industry-specific certifications or accreditation required for your business. ")
        title = st.text_area('List down the certifications you got')
    st.button("Completed task 10")
    if st.button("Continue with task 11"):
        st.switch_page("stage11.py")



        