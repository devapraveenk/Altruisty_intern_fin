import streamlit as st
def stage_13():
    st.header("STAGE 13")
    st.write(" 1. Compile a list of actionable insights and recommendations from customer reviews and surveys.")
    option = st.selectbox(
        ' Did you compile a list of actionable insights and recommendations from customer reviews and surveys?',
        ('Compiled', 'NO'))
    st.write('You selected:', option)
    if option=='Compiled':
        st.button("submit")
    if st.button("Completed task 1"):
        st.write(" 2. Prioritize the identified changes based on their potential impact on customer satisfaction and business objectives.")
        title = st.text_area('List the prioritized changes')
    if st.button("Completed task 2"):
        st.write(" 3. Collaborate with cross-functional teams to implement the necessary changes to products, services, or processes.")
        option = st.selectbox(
            'Did you collaborate with cross-functional teams to implement the necessary changes to products, services, or processes?',
            ('Collaborated', 'NO'))
        st.write('You selected:', option)
        if option=='Collaborated':
            st.button("next")
    if st.button("Completed task 3"):
        st.write(" 4. Communicate updates and changes to customers through email, social media, or other channels. ")
        option = st.selectbox(
            ' Did you communicate updates and changes to customers through email, social media, or other channels?',
            ('Communicated', 'NO'))
        st.write('You selected:', option)
        if option=='Communicated':
            st.button("next")
    if st.button("Completed task 4"):
        st.write(" 5. Monitor customer sentiment and feedback following the implementation of changes. ")
        option = st.selectbox(
            ' Did you monitor customer sentiment and feedback following the implementation of changes?',
            ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("next")
    if st.button("Completed task 5"):
        st.write(" 6. Measure the effectiveness of the changes in addressing customer concerns and improving satisfaction. ")
        option = st.selectbox(
            ' ?',
            ('Completed', 'NO'))
        st.write('You selected:', option)
        if option=='Completed':
            st.button("next")
    if st.button("Completed task 6"):
        st.write(" 7. Iterate on the changes based on ongoing feedback and performance metrics.")
        option = st.selectbox(
            ' Did you iterate on the changes based on ongoing feedback and performance metrics?',
            ('Iterated', 'NO'))
        st.write('You selected:', option)
        if option=='Iterated':
            st.button("next")
    if st.button("Completed task 7"):
        st.write(" 8. Solicit input from customer service teams or front-line employees on emerging issues or trends. ")
        option = st.selectbox(
            ' Did you get solicit input from customer service teams or front-line employees on emerging issues or trends?',
            ('Yes', 'NO'))
        st.write('You selected:', option)
        if option=='yes':
            st.button("next")
    if st.button("Completed task 8"):
        st.write(" 9. Continuously review and update products, services, and processes in response to evolving customer needs. ")
        option = st.selectbox(
            ' Are you continuously review and update products, services, and processes in response to evolving customer needs?',
            ('yes', 'not yet'))
        st.write('You selected:', option)
        if option=='yes':
            st.button("next")
    if st.button("Completed task 9"):
        st.write(" 10. Document the process and outcomes of updating changes based on customer reviews for future reference. ")
        title = st.text_area('Give the documentation of the above tasks')
    st.button("Completed task 10")
    if st.button("Continue with task 14"):
        st.switch_page("stage14.py")



        