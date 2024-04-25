import streamlit as st
def runevent():
    st.title("Events Update")

    st.subheader("Events")
    img=[['image/eveimage.webp', 'image/eveimage.webp','image/eveimage.webp','image/eveimage.webp'],['image/eveimage.webp', 'image/eveimage.webp','image/eveimage.webp','image/eveimage.webp'],['image/eveimage.webp', 'image/eveimage.webp','image/eveimage.webp','image/eveimage.webp'],['image/eveimage.webp', 'image/eveimage.webp','image/eveimage.webp','image/eveimage.webp']]
    Date=[['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23']]
    loc=[['chennai', 'tiruchi','tenkasi', 'ooty'],['madurai', 'theni','Location C', 'Location D'],['Location A', 'Location B','Location C', 'Location D'],['Location A', 'Location B','Location C', 'Location D']]
    c=1
    j=0
    for f in range(4):
            col1, col2,col3,col4,col5=st.columns(5)
            with col1:
                st.image(img[f][0], caption=f"Date: {Date[f][0]}, Location: {loc[f][0]}", width=120)
            with col2:
                st.image(img[f][1], caption=f"Date: {Date[f][1]}, Location: {loc[f][1]}", width=120)
            with col3:
                st.image(img[f][2], caption=f"Date: {Date[f][2]}, Location: {loc[f][2]}", width=120)
            with col4:
                st.image(img[f][3], caption=f"Date: {Date[f][3]}, Location: {loc[f][3]}", width=120)  
            with col5:
                if f==0:
                    if st.button("View More", key="home_button"):
                        st.markdown("[Home Page](http://localhost:8501//workspaces/event/main.py/Hello.py)")
                elif f==1:
                    if st.button("View More", key="home_button2"):
                        st.markdown("[Home Page](http://localhost:8501//workspaces/event/main.py/page2.py)")
                elif f==2:
                    if st.button("View More", key="home_button3"):
                        st.markdown("[Home Page](/workspaces/event/main.py/page2.py)")
                elif f==3:
                    if st.button("View More", key="home_button4"):
                        st.markdown("[Home Page](http://localhost:8501/main.py/page2.py)")
