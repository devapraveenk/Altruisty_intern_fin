import streamlit as st
def stage_8():
    st.header("STAGE 8")
    st.write(" 1. Define the objectives and scope of your market research.")
    title=st.text_area('What are your objectives and scope ?')
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Identify your target market segments and customer personas.")
        title = st.text_area('What is your target market segments ?')
    if st.button("Completed task 2"):
        st.write(" 3. Gather secondary research data from industry reports, market studies, and academic journals.")
        title = st.text_area('List out the secondary research data you gathered')
    if st.button("Completed task 3"):
        st.write(" 4. Conduct primary research through surveys, interviews, or focus groups. ")
        title = st.text_area('How did you conduct primary research and what is the feedback')
    if st.button("Completed task 4"):
        st.write(" 5. Analyze competitors and market trends to identify opportunities and threats. ")
        title = st.text_area('Who do you think your competitors and list their technology')
    if st.button("Completed task 5"):
        st.write(" 6. Assess the size and growth potential of your target market. ")
        title = st.text_area('What is the size and growth potential of your target market')
    if st.button("Completed task 6"):
        st.write(" 7. Investigate consumer behavior and preferences related to your product or service.")
        title = st.text_area('What information did you get from investigation')
    if st.button("Completed task 7"):
        st.write(" 8. Use data analytics tools to analyze market data and draw insights. ")
        title = st.text_area('What are the tools did you use and write down the analysis')
    if st.button("Completed task 8"):
        st.write(" 9. Validate your business assumptions through empirical research. ")
        title = st.text_area('What were your business assumptions through research')
    if st.button("Completed task 9"):
        st.write(" 10. Document your findings and insights to inform strategic decision-making. ")
        title = st.text_area('Write down the documentation part of this stage')
    st.button("Completed task 10")
    if st.button("Continue with task 9"):
        st.switch_page("stage9.py")



        