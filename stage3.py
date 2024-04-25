import streamlit as st
import pandas as pd
def stage_3():
    st.header("STAGE 3")
    st.write(" 1. Create a compelling pitch deck outlining the problem, solution, market opportunity, and business model.")
    st.write("Did you complete the below processs ?")
    data_df = pd.DataFrame(
            {
                "widgets": ["Problem statement","Solution", "market oppurunity", "Bussiness model"],
                "Completed": [False, False, False,False],
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
    if st.button("Completed task 1"):
        st.write(" 2. Design visually appealing slides with clear messaging.")
        st.text_area("Did you complete designing your slides ?")
        data_df = pd.DataFrame(
                {
                    "widgets": ["Tech stack", "Uniqueness", "Problem overview"],
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
    if st.button("Completed task 2"):
        st.write(" 3. Include relevant data, market research, and financial projections in the pitch deck.")
        st.write("Did you research the below following")
        data_df = pd.DataFrame(
                {
                    "widgets": ["Market research", "Market potential", "Financial projections"],
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
    if st.button("Completed task 3"):
        st.write(" 4. Tailor the pitch deck to the specific needs of potential investors. ")
        md= st.text_area('What are the specific needs of potential investors in your project ?', '')
    if st.button("Completed task 4"):
        st.write(" 5. Practice presenting the pitch deck to refine your delivery. ")
        md = st.text_area('List down the important points in you presentation', '')
    if st.button("Completed task 5"):
        st.write(" 6. Incorporate feedback from mentors or advisors to improve the pitch deck. ")
        md = st.text_area('What feedback did you get from advisors or mentors ?', '')
    if st.button("Completed task 6"):
        st.write(" 7. Ensure consistency in branding and messaging throughout the pitch deck.")
        md= st.text_area('What are the key points that make your product a brand ?', '')
    if st.button("Completed task 7"):
        st.write(" 8. Highlight the unique selling points and competitive advantages of your startup. ")
        md= st.text_area('List down the advantages of your project ', '')
    if st.button("Completed task 8"):
        st.write(" 9. Use storytelling techniques to engage investors and create a memorable impression. ")
        md= st.text_area('Create a story in the given tab and submit it', '')
    if st.button("Completed task 9"):
        st.write(" 10. Prepare additional materials, such as a one-pager or executive summary, to complement the pitch deck. ")
        md= st.text_area('Prepare draft papers or summary and enter in here ', '')
    if st.button("Completed task 10"):
        st.switch_page("stage4.py")



        