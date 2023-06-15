import streamlit as st
import openai

def _check_models():
    try:
        # Attempt to retrieve the list of models
        model_lst = openai.Model.list()
        return model_lst
    except Exception as e:
        # Exception handling
        return None

def _AddImageContent(Title, Src):
       st.header(Title)
       st.image(Src, width=200)
    

# Create Sidebar to configure OPEN AI API
__side_bar = st.sidebar
_open_ai_api_key = __side_bar.text_input('Please provide you OPEN AI API KEY : ', '...',  help = "...")
_max_tokens = __side_bar.number_input('Tokens : ')
_temperature = __side_bar.slider('Temperature', 0.0, 1.0, help = "This is the degree of randomness of the model's output.")
_model =  __side_bar.selectbox(
    "Select a Model",
    ("Email", "Home phone", "Mobile phone")
)
__side_bar.divider()



# Call the function
models = _check_models()
if models is not None:
    # Print the list of models if no errors occurred
    st.write("List of models:", models)



st.write()
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

tab1, tab2, tab3, tab4, tab5 = st.tabs([
   "Summarizing" 
   ,"Inferring"
   ,"Transforming"
   ,"Expanding"
   ,"Chatbot"
   ])

with tab1:
   _AddImageContent("Tab 1","https://static.streamlit.io/examples/cat.jpg")

with tab2:
   st.header("Tab 2")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("Tab 3")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
   st.header("Tab 4")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab5:
   st.header("Tab 5")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)