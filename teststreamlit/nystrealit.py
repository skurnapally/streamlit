import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#st.write
st.write('writing some text')


#magic 

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

# markdown
st.markdown('Streamlit is **_really_ cool**.')


#st.title
st.title('This is a title')

#st.header
st.header('This is a header')

#st.subheader
st.subheader('This is a subheader')

#st.caption
st.caption('This is a string that explains something above.')

# st.code

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')


#st.text
st.text('This is some text.')

#st.latex
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
     
#st.dataframe
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

#st.table

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

#st.metric
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

#st.json
st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })
 
#st.linechart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#st.areachart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

#st.bar_chart
chart_data = pd.DataFrame(
     [[1,2,3,4,5,6],[3,4,56,4,3,4],[1,2,3,4,3,34]],
     columns=["a", "b", "c","d","e","f"])

st.bar_chart(chart_data)

#st.pyplot
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
fig, ax = plt.subplots()
ax.scatter(x,y)
st.pyplot(fig)

# plotly

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

#st.map
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

#st.button
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#st.download
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
 
#st.checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
#st.radio
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'),index =2)

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
    
#st.selectbox
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#st.multiselect
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

#st.slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

values = st.slider(
     'Select a range of values',
     value=(datetime(2020, 1, 1, 9, 30),datetime(2020, 2, 1, 9, 30)))
st.write('Values:', values)

#st.select_slider
color = st.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('blue', 'red'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


#st.text_input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#st.number_input
number = st.number_input('Insert a number')
st.write('The current number is ', number)

#st.textarea
txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', txt)

d = st.date_input(
     "When's your birthday",
     datetime(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime(2019, 7, 6,8, 45))
st.write('Alarm is set for', t)

#st.fileuploader
from io import StringIO 
uploaded_file = st.file_uploader("Choose a file1")

if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
     
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)
     
#st.camera
cameras=st.checkbox('switch on camera')
if cameras:
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture)
cameras1=st.checkbox('switch on camera1') 
if cameras1:
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer as bytes:
        bytes_data = img_file_buffer.getvalue()
        # Check the type of bytes_data:
        # Should output: <class 'bytes'>
        st.write(type(bytes_data))


#st.color_picker
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

uploaded_file = st.file_uploader("Choose a file")

from PIL import Image

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Sunrise by the mountains')
    
#st.audio
audio=st.checkbox('want to listen my a song')
if audio:
    audio_file = open('Voodoo Badshah 320 Kbps.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
video=st.checkbox('wanna watch a video',key='daffa')
if video:
    video_file = open('Y2Mate.is - Konchem Istam Konchem Kastam Comedy-0KpM2WIWOLE-720p-1647504971861.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    


# Using object notation
add_selectbox = st.sidebar.selectbox("How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),key='Jaffa'
)

st.sidebar.daffa

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
    
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

for i in range(1,10):
    st.balloons()

for i in range(1,10):
    st.snow()