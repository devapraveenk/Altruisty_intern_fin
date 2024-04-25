import streamlit as st
import json
from streamlit_option_menu import option_menu


# def run():
#     st.set_page_config(
#         page_title="Streamlit quizz app",
#         page_icon="❓",
#     )

# if __name__ == "__main__":
#     run()
score=0
def quiz():
    # Custom CSS for the buttons
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        display: block;
        margin: 0 auto;
    </style>
    """, unsafe_allow_html=True)

    # Initialize session variables if they do not exist
    default_values = {'current_index': 0, 'current_question': 0, 'score': 0, 'selected_option': None, 'answer_submitted': False}
    for key, value in default_values.items():
        st.session_state.setdefault(key, value)

    # Load quiz data
    with open('quize_data.json', 'r', encoding='utf-8') as f:
        quiz_data = json.load(f)

    def restart_quiz():
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False

    def submit_answer():
        global score
        # Check if an option has been selected
        if st.session_state.selected_option is not None:
            # Mark the answer as submitted
            st.session_state.answer_submitted = True
            # Check if the selected option is correct
            if st.session_state.selected_option == quiz_data[st.session_state.current_index]['answer']:
                if quiz_data[st.session_state.current_index]['question']=="Did you generate a novel concept for your business idea?":
                    st.session_state.score += 10
                    
                    score+=10
                elif quiz_data[st.session_state.current_index]['question']=="Did you design the workflow for your product or service?":
                    st.session_state.score += 10
                    score+=10
                elif quiz_data[st.session_state.current_index]['question']=="Did you create a prototype design to visualize your product/service?":  
                    st.session_state.score += 10
                    score+=10
                elif quiz_data[st.session_state.current_index]['question']=="Did you create a pitch deck to present your business idea to potential stakeholders?":  
                    st.session_state.score += 10
                    score+=10
                elif quiz_data[st.session_state.current_index]['question']=="Did you develop a prototype of your product/service?":  
                    st.session_state.score += 20
                    score+=20
                elif quiz_data[st.session_state.current_index]['question']=="Did you conduct a proof of concept to validate your idea's feasibility?":  
                    st.session_state.score += 20
                    score+=20
                elif quiz_data[st.session_state.current_index]['question']=="Did you analyze the market to identify opportunities and threats?":  
                    st.session_state.score += 20
                    score+=20
                elif quiz_data[st.session_state.current_index]['question']=="Did you conduct market research to understand your target audience?":  
                    st.session_state.score += 20
                    score+=20
                elif quiz_data[st.session_state.current_index]['question']=="Did you obtain copyright or patent protection for your innovation?":  
                    st.session_state.score += 20
                    score+=20
                elif quiz_data[st.session_state.current_index]['question']=="Did you register your company legally?":  
                    st.session_state.score += 30
                    
                    score+=30
                elif quiz_data[st.session_state.current_index]['question']=="Did you implement your business idea on a small scale?":  
                    st.session_state.score += 30
                    
                    score+=30
                elif quiz_data[st.session_state.current_index]['question']=="Did you gather feedback from customers through reviews and surveys?":  
                    st.session_state.score += 30
                    
                    score+=30
                elif quiz_data[st.session_state.current_index]['question']=="Did you incorporate the suggested changes based on customer feedback?":  
                    st.session_state.score += 40
                    
                    score+=40
                elif quiz_data[st.session_state.current_index]['question']=="Did you prepare an investor pitch deck to attract funding?":  
                    st.session_state.score += 40
                    
                    score+=40
                elif quiz_data[st.session_state.current_index]['question']=="Did you secure funds from investors, angel investors, venture capital, or grants?":  
                    st.session_state.score += 40
                 
                    score+=40
        else:
            # If no option selected, show a message and do not mark as submitted
            st.warning("Please select an option before submitting.")

    def next_question():
        st.session_state.current_index += 1
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False

    # Title and description
    st.title("Assessment Test")

    # Progress bar
    progress_bar_value = (st.session_state.current_index + 1) / len(quiz_data)
    st.metric(label="Score", value=f"{st.session_state.score} / {350}")
    # st.progress(progress_bar_value)

    # Display the question and answer options
    try:

        question_item = quiz_data[st.session_state.current_index]
        st.subheader(f"Question {st.session_state.current_index + 1}")
        st.title(f"{question_item['question']}")
        st.write(question_item['information'])

        st.markdown(""" _""")

        # Answer selection
        options = question_item['options']
        correct_answer = question_item['answer']

        if st.session_state.answer_submitted:
            for i, option in enumerate(options):
                label = option
                if option == correct_answer:
                    st.success(f"{label} (done)")
                elif option == st.session_state.selected_option:
                    st.error(f"{label} (done)")
                else:
                    st.write(label)
        else:
            for i, option in enumerate(options):
                if st.button(option, key=i, use_container_width=True):
                    st.session_state.selected_option = option

        st.markdown(""" _""")

        # Submission button and response logic
        if st.session_state.answer_submitted:
            if st.session_state.current_index < len(quiz_data) - 1:
                st.button('Next', on_click=next_question)
                
            else:
                st.write(f"Quiz completed! Your score is: {st.session_state.score} / {350}")
                st.session_state.current_index+=1
                if st.session_state.score==350:
                    st.write("You Are In Stage 15")
                elif st.session_state.score>=330:
                    st.write("You Are In Stage 14")
                elif st.session_state.score>=300:
                    st.write("You Are In Stage 13")
                elif st.session_state.score>=270:
                    st.write("You Are In Stage 12")
                elif st.session_state.score>=250:
                    st.write("You Are In Stage 11")
                elif st.session_state.score>=230:
                    st.write("You Are In Stage 10")
                elif st.session_state.score>=200:
                    st.write("You Are In Stage 9")
                elif st.session_state.score>=170:
                    st.write("You Are In Stage 8")
                elif st.session_state.score>=150:
                    st.write("You Are In Stage 7")
                elif st.session_state.score>=120:
                    st.write("You Are In Stage 6")
                elif st.session_state.score>=100:
                    st.write("You Are In Stage 5")
                elif st.session_state.score>=80:
                    st.write("You Are In Stage 4")
                elif st.session_state.score>=60:
                    st.write("You Are In Stage 3")
                elif st.session_state.score>=30:
                    st.write("You Are In Stage 2")
                elif st.session_state.score>=0:
                    
                    st.write("You Are In Stage 1")

                
        else:
            if st.session_state.current_index < len(quiz_data):
                st.button('Submit', on_click=submit_answer)
    except:
        st.write("Completed")

    return score
    
   

def move():
        if st.session_state.current_index == 15:
            return st.session_state.current_index
        # return False
# def score():
#     return st.session_state.score


