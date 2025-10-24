import streamlit as st 
import random 

# title 
st.title('My Project')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('MinhTri')
st.caption('Do Minh Tri')

st.divider()

st.markdown('# heading 1')
st.markdown('[minhtri](https://www.facebook.com/)')
st.markdown("""
    1.ML
    2.DL    
""")
st.markdown(r'$ \sqrt{2x} $')

st.divider()

st.latex('\sqrt{2x}')
st.write('Do Minh Tri')

st.divider()

st.code("""
    import random 
    value = random.randint(1 , 10)
    print(value)
""")
# nếu khối lệnh quá dài 
with st.echo() : 
    st.write('this is a text')
    def get_name() : 
        return 'tri'

    name = get_name()
    st.write(name)

    st.divider() 
# st.logo('module 1 /w4/T4/Description/source/dog.jpeg')
# st.image('./dog.jpeg')    

st.divider() 

def get_fullname() : 
    return st.write('tri')

ok = st.checkbox('ok' , on_change=get_fullname) 
if ok : 
    st.write('Thanks')

st.radio('your fav : ' ,['yellow', 'blue'] ,captions = ['vàng' , 'xanh'])
st.selectbox('your contact ',['eamil , address'])
options = st.multiselect('colors' ,['red' ,'yellow' ,'blue'] ,['red'])
print(options)
st.select_slider('your colors' ,[1 , 2 , 3 , 4 , 5 , 6 , 7, 8, 9 ,10])

st.divider() 

if st.button('hello') : 
    st.write('2')
else : 
    pass 

st.text_input('your name :' ,value = 'enter your name')

st.divider() 

upload_file = st.file_uploader('choose file', accept_multiple_files = True)
for file in upload_file : 
    read_f = file.read() 
    st.write("file name : " , file.name)                      

st.divider() 

col1 , cols = st.columns(2) 

st.divider() 

st.write(st.session_state())