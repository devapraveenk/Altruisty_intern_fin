import streamlit as st
def stage_14():
    st.header("STAGE 14")
    st.write(" 1. Review and update your existing pitch deck based on feedback from previous presentations.")
    title = st.text_area("Did you review and update your existing pitch deck based on feedback from previous presentations")
    st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Tailor the pitch deck to the specific interests and requirements of potential investors. ")
        t=st.text_area("List down the points that you tailored for the pitch deck to the specific interests and requirements of potential investors ")
    if st.button("Completed task 2"):
        st.write(" 3. Highlight key milestones, achievements, and growth metrics since the last pitch. ")
        title = st.text_area('List down the key milestones, achievements, and growth metrics since the last pitch')
    if st.button("Completed task 3"):
        st.write(" 4. Incorporate updated market research, financial projections, and competitive analysis. ")
        title = st.text_area('List down the updated market research, financial projections, and competitive analysis')
    if st.button("Completed task 4"):
        
        st.write("5. Showcase any partnerships, endorsements, or awards received since the last pitch. ")
        title = st.text_area('Give the points of showcasing partnerships, endorsements, or awards received since the last pitch.')
    if st.button("Completed task 5"):
        st.write(" 6. Include case studies or testimonials from satisfied customers or early adopters.")
        title = st.text_area('Write down the case studies or testimonials from satisfied customers or early adopters ')
    if st.button("Completed task 6"):
        st.write(" 7. Present a clear road map for future development and expansion.")
        title = st.text_area('List down the points of presenting a clear road map for future development and expansion ')
    if st.button("Completed task 7"):
        st.write(" 8. Address any concerns or objections raised by previous investors. ")
        option = st.selectbox(
            ' Did you address any concerns or objections raised by previous investors ?',
            ('Yes', 'NO'))
        st.write('You selected:', option)
        if option=='Yes':
            st.button("next") 
    if st.button("Completed task 8"):
        st.write(" 9. Practice delivering the pitch with confidence and conviction.")
        title = st.text_area('List down the points you practiced for delivering the pitch with confidence and conviction')
    if st.button("Completed task 9"):
        st.write(" 10. Prepare for questions and objections from investors during the pitch.")
        option = st.selectbox(
            ' Did you prepare for questions and objections from investors during the pitch ?',
            ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("next")
    if st.button("Completed task 10"):
        st.switch_page("tage15.py")
            