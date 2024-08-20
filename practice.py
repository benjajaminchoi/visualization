import openai
import streamlit as st


api_key = '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'

#if 'thumb' not in st.session_state:
st.session_state.thumb = 0

st.header('''
         hello world
         ''')

if st.button('좋아요👍'):
    st.session_state.thumb += 1

st.image('pic1.jpg')

st.write(f'좋아요: {st.session_state.thumb}')
