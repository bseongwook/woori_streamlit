# 2023-12-05
# https://cheat-sheet.streamlit.app/  공홈 설명서

import streamlit as st
import pandas as pd  # st은 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬 코드로 구현됩니다.

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# 입력
st.title('1. 입력버튼들')

# 버튼을 누르면 데이터프레임이 등장하도록 로직을 만들어주세요
button_result = st.button('Hit me') # 누르면 True로 바뀜
if button_result:
    st.data_editor(data) # 등장한 표를 누르면 다시 button_result가 False로 바뀜

check_button = st.checkbox('Check me out') # 누를때마다 T F 토글, 다른거 클릭해도 값 안바뀜
if check_button:
    st.data_editor(data) 

st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])

gogi_list = ['1고기', '2고기', '3고기']
img_list = ['https://imgur.com/VjorYAV.png', 
               'https://imgur.com/sOSRtyI.png', 
               'https://imgur.com/WYX34wL.png']

search = st.text_input('Enter some text')
if search != '':
    for i in gogi_list:
        if search in i:
            st.image(img_list[gogi_list.index(i)])

# st.image('https://imgur.com/VjorYAV.png') # 주소 뒤에 png 붙이기

st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
# st.download_button('On the download', data) # 해당 버튼을 통해 data를 다운 받을 수 있는 버튼
st.download_button(
    label = "On the download",
    data = data.to_csv(),
    file_name = 'app_df.csv',
    mime = 'text/csv',
)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

# 출력
