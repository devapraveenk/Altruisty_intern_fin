import streamlit as st
def stage_15():
    st.header("STAGE 15")
    st.write(" 1.Identify potential investors or funding sources aligned with your startup's stage and industry.")
    title = st.text_area("Did you identify potential investors or funding sources aligned with your startup's stage and industry")
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Research the investment criteria and preferences of each potential investor.")
        t=st.text_area("What was you research ?")
    if st.button("Completed task 2"):
        st.write(" 3. Develop a targeted approach for reaching out to investors, whether through warm introductions or networking events.")
        title = st.text_area('What did you develop a targeted approach for reaching out to investors, whether through warm introductions or networking events')
    if st.button("Completed task 3"):
        st.write(" 4. Prepare a compelling investment proposal outlining your business opportunity and funding requirements. ")
        title = st.text_area('List down the points you prepared for a compelling investment proposal outlining your business opportunity and funding requirements')
    if st.button("Completed task 4"):
        st.write(" 5. Schedule meetings or pitch sessions with potential investors to present your proposal. ")
        title = st.text_area('Write down how are you going to schedule meet or pitch sessions with potential investors to present your proposal')
    if st.button("Completed task 5"):
        st.write(" 6. Clearly articulate your value proposition and growth potential to investors.")
        title = st.text_area('List down how you are going to clearly articulate your value proposition and growth potential to investors')
    if st.button("Completed task 6"):
        st.write(" 7. Negotiate terms and conditions of investment agreements, including valuation, equity stake, and board representation.")
        title = st.text_area('What are the terms you are going to negotiate of investment agreements, including valuation, equity stake, and board representation')
    if st.button("Completed task 7"):
        st.write(" 8. Conduct due diligence on potential investors to assess their track record and reputation. ")
        option = st.selectbox(
            ' ?',
            ('Yes', 'No'))
        st.write('You selected:', option)
        if option=='Yes': 
            st.button("")
            
    if st.button("Completed task 8"):
        st.write(" 9. Secure commitments or term sheets from interested investors. ")
        option = st.selectbox(
        ' ?',
        ('Secured', 'No'))
        st.write('You selected:', option)
        if option=='Secured': 
            st.button("next")
            
    if st.button("Completed task 9"):

        st.write(" 10. Close the investment round and allocate funds towards business growth and expansion. ")
        option = st.selectbox(
        ' ?',
        ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("proceed")
    if st.button("Completed task 10"):
        st.write("**YAYYY YOU HAVE COMPLETED ALL THE STAGES!!!!**")



        