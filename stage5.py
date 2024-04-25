import streamlit as st
def stage_5():
    st.header("STAGE 5")
    st.write(" 1. Translate the product/service workflow design into a clickable prototype.")
    md = st.text_area('Did you start the process and how ?', '')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Use prototyping tools such as Sketch, Figma, or Adobe XD to create interactive mock-ups.")
        st.text_area("What tools are you using ?")
    if st.button("Completed task 2"):
        st.write(" 3. Focus on creating a seamless and intuitive user experience in the prototype.")
        st.text_area("What research did you do and understnd ?")
    if st.button("Completed task 3"):
        st.write(" 4. Incorporate feedback from stakeholders to refine the prototype design. ")
        st.text_area("what was the feedback")
    if st.button("Completed task 4"):
        st.write(" 5. Ensure consistency in design elements and branding. ")
        st.text_area("What design made your product a brand")
    if st.button("Completed task 5"):
        st.write(" 6. Test the prototype with potential users to identify usability issues. ")
        option = st.selectbox(
            ' ?',
            ('YES', 'NO'))
        st.write('You selected:', option)
        if option=='YES':
            st.button("next")
    if st.button("Completed task 6"):

        st.write(" 7. Iterate on the prototype based on user feedback.")
        st.text_area("What was the feedback ?")
    if st.button("Completed task 7"):
        st.write(" 8. Validate the prototype against the initial concept and user requirements. ")
        st.text_area("How did you refine your prototype based on the feedback ?")
    if st.button("Completed task 8"):
        st.write(" 9. Document the design decisions and rationale behind the prototype. ")
        st.text_area("Write your document")
    if st.button("Completed task 9"):
        st.write(" 10. Prepare the prototype for presentation to investors or stakeholders. ")
        option = st.selectbox(
            ' ?',
            ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("Completed task 10")
    if st.button("Continue with task 6"):
        st.switch_page("stage6.py")



        