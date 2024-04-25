import streamlit as st
from streamlit_option_menu import option_menu

def show_funding_schemes():
    st.title("Funding Schemes")
    selection = option_menu(
        menu_title="",
        options=['About',"Seed Funding Program", "Venture Capital Funding", "Government Grants"],
        icons=["house", "book", "envelope",'book'], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",
    )

    st.subheader("Explore different funding opportunities for startups and businesses.")

    link=['https://www.startupindia.gov.in','https://www.investindia.gov.in','https://www.msme.gov.in/']
    if selection == 'About':
        st.write("Here we provides some important funding Details about your projects")
    if selection=='Seed Funding Program':
        st.write('Provides funding for early-stage startups.')
        st.write('More info:',link[0])
    if selection=='Venture Capital Funding':
        st.write('Investment from venture capital firms in exchange for equity.')
        st.write('More info:',link[1])
    if selection=='Government Grants':
        st.write('Financial assistance provided by the government to support specific projects or industries.')
        st.write('More info:',link[2])


def main():
    show_funding_schemes()

if __name__ == "__main__":
    main()