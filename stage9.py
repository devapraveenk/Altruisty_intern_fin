import streamlit as st
def stage_9():
    st.header("STAGE 9")
    st.write(" 1. Evaluate the competitive landscape to understand existing players and their market share.")
    title = st.text_area('Information you got from evaluation')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Identify key market trends, drivers, and challenges affecting your industry.")
        title = st.text_area('What are the key market trends, drivers, and challenges')
    if st.button("Completed task 2"):
        st.write(" 3. Assess the pricing strategies and positioning of competitors in the market.")
        title = st.text_area('List down the pricing stratergies and positioning of competitors in the market')
    if st.button("Completed task 3"):
        st.write(" 4. Analyze customer needs and preferences to identify market opportunities. ")
        title = st.text_area('What did you analyse?')
    if st.button("Completed task 4"):
        st.write(" 5. Conduct a SWOT analysis to assess your strengths, weaknesses, opportunities, and threats. ")
        option = st.selectbox(
            ' ?',
            ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("next")
    if st.button("Completed task 5"):
        st.write(" 6. Determine the market entry barriers and regulatory environment. ")
        title = st.text_area('What are the market entry barriers ?')
    if st.button("Completed task 6"):
        st.write(" 7. Evaluate potential distribution channels and partnerships to reach your target market.")
        title = st.text_area('How did youu evaluate and list down')
    if st.button("Completed task 7"):
        st.write(" 8. Estimate the market size and growth potential for your product or service. ")
        title = st.text_area('What is the market size estimation ?')
    if st.button("Completed task 8"):
        st.write(" 9. Identify emerging market segments or niche markets to target. ")
        title = st.text_area('What are the market segments or niche markets to target ?')
    if st.button("Completed task 9"):
        st.write(" 10. Develop a competitive strategy based on your market analysis findings. ")
        title = st.text_area('After developing a competitive stratergy, list down them')
    st.button("Completed task 10")
    if st.button("Continue with task 10"):
        st.switch_page("stage10.py")



        