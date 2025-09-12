import streamlit as st
from summerizer import  summerization_main
from speechToText import Record_Question,ouput_text
from qanda import ask_question

if 'ok_disabled' not in st.session_state:
    st.session_state.ok_disabled = True

if 'button_disabled' not in st.session_state:
    st.session_state.button_disabled = True
    
if 'summery' not in st.session_state:
    st.session_state.summery = None
    
if 'text' not in st.session_state:
    st.session_state.text = None

summery = None
text = None
inputs = st.text_input("enter your text here")
if st.button("submit"):
    if inputs: 
        summery =  summerization_main(inputs)
        st.session_state.button_disabled = False
        st.session_state.summery = summery
    else: st.markdown("please enter something to summerize and tell")
    
if st.button("Mic",disabled = st.session_state.button_disabled):
#     with st.spinner("🎙️ Please talk..."):
        text = Record_Question()
        st.session_state.text = text
        st.session_state.ok_disabled = False
#     st.success("✅ Done Listening!")
        st.write("You said:", text)
#     ouput_text(text)
    
if st.button("ok",disabled = st.session_state.ok_disabled):
    if st.session_state.summery and st.session_state.text:
        ans = ask_question(st.session_state.summery, st.session_state.text)
        st.write(ans)
    else:
        st.warning("⚠️ Missing summary or mic input")
        
        
        
        