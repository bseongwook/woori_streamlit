import streamlit as st
import pandas as pd 

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.write(add_selectbox)
st.write(add_radio)

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1]) 
# 전체 중 각 숫자의 비율만큼 쓰겠다.
# col1 is wider

# Using 'with' notation: 이미지 크기를 알아서 조절, 따로 조절도 가능
with col1:
    st.write('https://imgur.com/VjorYAV.png')
with col2:
    st.write('This is column 2')
with col3:
    st.write('This is column 3')    