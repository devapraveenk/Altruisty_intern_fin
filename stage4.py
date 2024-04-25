import streamlit as st
def stage_4():
    st.header("STAGE 4")
    st.write(" 1. Map out the user journey to understand how customers will interact with your product or service.")
    title = st.text_input('What the main points to make customer interact with your product ?', '')
    if st.button("Completed task 1"):

        st.write(" 2. Identify key touch points and pain points in the workflow.")
        md = st.text_area('List out the points that makes it diificult for you in the workflow', '')
    if st.button("Completed task 2"):

        st.write(" 3. Design wire frames or mock ups to visualize the user experience.")
        st.link_button("To refer about designing wire frames or mockups","https://zapier.com/blog/best-wireframe-tools/")
    if st.button("Completed task 3"):

        st.write(" 4. Define the features and functionalities of the product or service. ")
        title = st.text_input('What are your features and functionalities ? ', '')
    if st.button("Completed task 4"):
        st.write(" 5. Create a flowchart or diagram illustrating the workflow process. ")
        option = st.selectbox(
            ' ?',
            ('YES', 'NO'))
        st.write('You selected:', option)
        st.write("To design your own flowchart do in canva")
    if st.button("Completed task 5"):
        st.write(" 6. Consider potential integration with other tools or platforms. ")
        md = st.text_area('What are your considerations ?')
    if st.button("Completed task 6"):
        st.write(" 7. Collaborate with designers and developers to refine the workflow design.")
        option = st.selectbox(
            ' ?',
            ('Developed', 'Not yet'))
        st.write('You selected:', option)
        if option=='Developed':
            st.button("next")
    if st.button("Completed task 7"):
        st.write(" 8. Test the workflow design with real users to gather feedback. ")
        md= st.text_area('What are the feedbacks you got ?')
    if st.button("Completed task 8"):
        st.write(" 9. Iterate on the design based on user testing results.")
        md = st.text_area('What was the repeated feedbacks you got ?')
    if st.button("Completed task 9"):
        st.write(" 10. Document the finalized product/service workflow for future reference.")
        md = st.text_area('Write your document below')
    if st.button("Continue with task 5"):
        st.switch_page("stage5.py")



        
        