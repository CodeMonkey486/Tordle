import streamlit as st
import pandas as pd
import random
import datetime

def update_first():
    
    if st.session_state.first.upper()!=Word[0].upper():
        st.session_state.first=""
    
    if st.session_state.second.upper()!=Word[1].upper():
        st.session_state.second=""
   
    if st.session_state.third.upper()!=Word[2].upper():
        st.session_state.third=""
    
    if st.session_state.fourth.upper()!=Word[3].upper():
        st.session_state.fourth=""
    
    if st.session_state.fifth.upper()!=Word[4].upper():
        st.session_state.fifth=""
    
current_time = datetime.datetime.now()
num=current_time.day%10



df=pd.read_excel(r'C:\Users\19209\Wordy/Test.xlsx')
Question=df.Question.tolist()
Answer=df.Answer.tolist()
#num=random.randrange(1, 9)  

st.markdown("***")

Word=Answer[num]


Score=0

html_temp = """
<div style="background-color:black;padding:1.5px">
<h2 style="color:white;text-align:center;">Welcome to Tordle! </h2>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.write(Question[num])



#st.info("Trivia question with a 5 letter answer that can be solved like Wordle")

st.sidebar.image("Brainy.jpg")
#st.sidebar.markdown("<img src="Brainy.jpg" alt="Paris" class="center">",unsafe_allow_html=True)

st.sidebar.markdown("<h5 style='text-align: center; color: White;'>Are you good at solving Trivia and Word puzzles?</h5>", unsafe_allow_html=True)

st.sidebar.markdown("<h5 style='text-align: center; color: White;'>Guess the 5 letter answer and hit Submit</h5>", unsafe_allow_html=True)

st.sidebar.markdown("<h5 style='text-align: center; color: White;'>Incorrect letters disappear</h5>", unsafe_allow_html=True)
#st.sidebar.markdown("<h5 style='text-align: center; color: White;'>You have unlimited tries</h5>", unsafe_allow_html=True)



    
col1,col2,col3,col4,col5=st.columns(5)

with col1:
    st.text_input("",max_chars=1, key='first')

with col2:    
    st.text_input("",max_chars=1, key='second')
    
with col3:
    st.text_input("",max_chars=1, key='third')

with col4:    
    st.text_input("",max_chars=1, key='fourth')
    
with col5:
    st.text_input("",max_chars=1, key='fifth')

st.button(label="Submit", key=None, help=None, on_click=update_first)
   
if st.session_state.first.upper()==Word[0].upper():
        Score=Score+1
    
if st.session_state.second.upper()==Word[1].upper():
        Score=Score+1
if st.session_state.third.upper()==Word[2].upper():
        Score=Score+1
        
    
if st.session_state.fourth.upper()==Word[3].upper():
          Score=Score+1
    
if st.session_state.fifth.upper()==Word[4].upper():
        Score=Score+1
        

if Score==5:
        st.balloons()
        
        


      


