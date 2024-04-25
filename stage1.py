import streamlit as st
import pandas as pd
import stage2
def stage_1():
        st.title("STAGE 1")
        st.write("1. Brainstorm potential business ideas")
        title = st.text_input('Project title', '')
        st.button("submit")
        if st.button("Completed task 1"):
                st.write("2.Evaluate market demand and feasibility of each idea.")
                st.write('Give the market demand of your product')
                md = st.text_area('')

        if st.button("Completed task 2"):
                st.write("3. Conduct market research to validate the viability of the chosen idea.")
                title=st.text_input('what did you conclude from your research','')
        if st.button("Completed task 3"):
        
                st.write(" 4. Define your target audience and their pain points.")
                option = st.selectbox('What is your target audience?',
                        ('Less 10k', 'Less 50k', 'More than 1 lakh'))
                st.write('You selected:', option)
                st.button("selected")
        if st.button("Completed task 4"):
                st.write(" 5. Refine the chosen idea based on market feedback.")
                st.write('What refinement did you do?')
                md = st.text_area('')
                st.button("done")
        if st.button("Completed task 5"): 
        
                st.write(" 6. Create a detailed business plan outlining the idea, target market, and revenue model.")
                data_df = pd.DataFrame(
                {
                "widgets": ["Planned idea", "Planned target market", "Planned revenue model"],
                "Completed": [False, False, False],
                }
                )
                st.data_editor(
                data_df,
                column_config={
                "favorite": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your *favorite* widgets",
                default=False,
                )
                },
                disabled=["widgets"],
                hide_index=True,
                )


        if st.button("Completed task 6"):

        
                st.write("7. Conduct a SWOT analysis to assess strengths, weaknesses, opportunities, and threats.")
                title=st.text_input('1.What are the strengths ?','')
                title=st.text_input('2. What are the weakness ?','')
                title=st.text_input('2. What are the opportunities ?','')
                title=st.text_input('2. What are the threats ?','')

        if st.button("Completed task 7"):
                st.write(" 8. Seek feedback from mentors or industry experts on your idea.")
                st.write('What was the best feedback suggested by experts ?')
                md = st.text_area('')

        if st.button("Completed task 8"):
        
                st.write("9. Consider potential scalability and long-term sustainability of the idea.")
                md = st.text_area('List down the potential scalability')
                md = st.text_area('What is the long-term sustainability of your idea ?')

        if st.button("Completed task 9"):
                st.write("10. Perform a competitive analysis to understand the landscape.")
                md = st.text_area('What information did you get by competitive analysis ?')

        if st.button("Completed task 10"):
                stage2.stage_2()

                            