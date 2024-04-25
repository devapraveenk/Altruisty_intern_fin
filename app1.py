import streamlit as st
import Funding_Page
from streamlit_option_menu import option_menu
import Hello
from chatbot import re
import streamlitpractice
import stage1
import stage2
import stage3
import stage4
import stage5
import stage6
import stage7
import stage8
import stage9
import stage10
import stage11
import stage12
import stage13
import stage14
import stage15
import basicdetail
import Event
import startuppage
import idea_evaluation

# score1=Hello.score()
def base():
    class MultiApp:



        def __init__(self):
            self.apps = []

        def add_app(self, title, func):

            self.apps.append({
                "title": title,
                "function": func
            })


        def run():
                # app = st.sidebar(
            with st.sidebar:        
                    select = option_menu(
                        menu_title='Main Menu',
                        options=["Quiz",'Tasks','Chatbot','Idea Evaluation','Fundings','Events','Start-Ups','Basic Details','FeedBack'],
                        icons=['book','clipboard-fill','chat-fill','tools','flag-fill','trophy-fill','minecart','tag-fill','file-earmark-person-fill'],
                        menu_icon='house',
                        default_index=0,
                        
                        )
            # q=0
            if select == "Quiz":
                global score
                score=Hello.quiz()
                # st.write()
            
            if Hello.move()==15:
                    if select == "Chatbot":
                         re()
                    if select=='FeedBack':
                      streamlitpractice.feedback()

                    if select=='Fundings':
                         Funding_Page.main()
                    
                    if select == 'Basic Details':
                         basicdetail.Basic_Details()
                    
                    if select == 'Events':
                         Event.runevent()
                    if select =='Start-Ups':
                         startuppage.startuprun()
                    
                    if select == 'Idea Evaluation':
                         idea_evaluation.idea()


                    if select=='Tasks':
                        # st.write(q)
                        if score==350:
                            stage15.stage_15()
                        elif score>=330:
                             stage14.stage_14()
                        elif score>=300:
                             stage13.stage_13()
                        elif score>=270:
                             stage12.stage_12()
                        elif score>250:
                             stage11.stage_11()
                        elif score>=230:
                             stage10.stage_10()
                        elif score>=200:
                             stage9.stage_9()
                        elif score>=170:
                             stage8.stage_8()
                        elif score>=150:
                             stage7.stage_7()
                        elif score>=120:
                             stage6.stage_6()
                        elif score>=100:
                             stage5.stage_5()
                        elif score>=80:
                             stage4.stage_4()
                        elif score>=60:
                             stage3.stage_3()
                        elif score>=30:
                             stage2.stage_2()
                        elif score>=0:
                             stage1.stage_1()
                        
                        
                              
            else:
                st.write("Complete The Quiz first")
                                
        run() 