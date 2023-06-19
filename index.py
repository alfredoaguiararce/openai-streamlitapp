import streamlit as st
import time
import openai

# Create Sidebar to configure OPEN AI API
__side_bar = st.sidebar

# `__models` is a list of different models available in OpenAI's GPT-3 API. These models have
# different capabilities and performance levels. The list is used in the Streamlit app to allow the
# user to select a specific model to use for generating text.
__models  = [
                "gpt-3.5-turbo"
                ,"gpt-3.5-turbo-0301"
                ,"gpt-3.5-turbo-0613"
                ,"gpt-3.5-turbo-16k"
                ,"gpt-3.5-turbo-16k-0613"
            ]

# Functions
def get_completion(prompt, model="gpt-3.5-turbo-16k", temperature=0):
    """
    This function uses OpenAI's chat completion API to generate a response to a given prompt using a
    specified model and temperature.
    
    :param prompt: The text prompt or message that you want to send to the OpenAI chatbot for completion
    :param model: The name of the OpenAI language model being used for text generation. In this case, it
    is set to "gpt-3.5-turbo-16k", defaults to gpt-3.5-turbo-16k (optional)
    :param temperature: The temperature parameter controls the degree of randomness or creativity in the
    model's output. A higher temperature value will result in more diverse and unexpected responses,
    while a lower temperature value will result in more conservative and predictable responses. The
    default value is 0, which means the model will always output the most likely, defaults to 0
    (optional)
    :return: The function `get_completion` returns a string, which is the response generated by the
    OpenAI chatbot model based on the given prompt.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def check_openai(key,model="gpt-3.5-turbo-16k",max_tokens=5, temperature=0):
    """
    The function checks if an OpenAI API key is valid by attempting to create a completion with
    specified parameters.
    
    :param key: The OpenAI API key that is required to access the OpenAI API
    :param model: The OpenAI language model to use for text generation. In this case, the default model
    is "gpt-3.5-turbo-16k", defaults to gpt-3.5-turbo-16k (optional)
    :param max_tokens: The maximum number of tokens (words or symbols) that the OpenAI API will generate
    in response to a prompt, defaults to 5 (optional)
    :param temperature: Temperature is a parameter used in OpenAI's language models to control the
    creativity and randomness of the generated text. It determines how much the model should deviate
    from the most likely next word when generating text. A higher temperature value will result in more
    creative and diverse output, while a lower temperature value will, defaults to 0 (optional)
    :return: a boolean value. If the OpenAI API key is valid and the API call is successful, it will
    return True. If there is an error with the API call, it will return False and display the error
    message in the sidebar.
    """
    openai.api_key = key
    test_messages = [{"role": "user", "content": "Test"}]
    try:
        openai.ChatCompletion.create(
            model=model,
            messages=test_messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        __side_bar.success('Open Ai configured!', icon="✅")
        return True
    except Exception as e:
        __side_bar.error(f'This is an Open ai Error : {str(e)}', icon="🚨")
        return False


# This code block creates a sidebar in the Streamlit app interface that allows the user to configure
# the OpenAI API. It includes text input fields for the OpenAI API key, a number input field for the
# maximum number of tokens, a slider for the temperature parameter, and a select box for choosing the
# OpenAI language model to use. When the user clicks the "Configure Open AI" button, the
# `check_openai` function is called to verify the API key and display a success or error message in
# the sidebar.
__side_bar.header("Open Ai Quick config")
_open_ai_api_key = __side_bar.text_input('Please provide you OPEN AI API KEY : ', '',  help = "...")
_max_tokens = int(__side_bar.number_input('Tokens : ', step=1))
_temperature = __side_bar.slider('Temperature', 0.0, 1.0, help = "This is the degree of randomness of the model's output.")
_model = __side_bar.selectbox("Models:", options=__models)

if __side_bar.button('Configure Open AI') and _open_ai_api_key != '':
    check_openai(_open_ai_api_key, _model, _max_tokens, _temperature)
    __side_bar.divider()



# `tab1, tab2, tab3, tab4, tab5 = st.tabs([...])` creates five tabs in the Streamlit app interface
# with the labels "Summarizing", "Inferring", "Transforming", "Expanding", and "Chatbot". Each tab can
# be clicked to display different content or functionality within the app. The variables `tab1`,
# `tab2`, `tab3`, `tab4`, and `tab5` are assigned to the corresponding tabs, which can be used to
# display content or widgets specific to each tab.
tab1, tab2, tab3 = st.tabs([
   "Summarizing" 
   ,"Inferring"
   ,"Transforming"
#    ,"Expanding"
#    ,"Chatbot"
   ])


# ========================================[Summarizing TAB]===============================================================================
with tab1:
    st.header("Summarizing")
    st.write("Use Chat Gpt to summarize text with delimiter number of words or not.")
    st.divider()

    _txt_to_be_summarized = st.text_area('Text to summarize : ', '')
    # Enable/disable checkbox based on a condition
    _is_words_limited = st.checkbox("Limit words")
    _total_words = None

    if _is_words_limited:
        _total_words = int(st.number_input('Max words: ',min_value=1, step=1, help="Number of words you want in your summary."))
        _summarize_prompt = f"""
        Your task is to generate a short summary of a text

        Summarize the text below, delimited by triple 
        backticks. in at most {_total_words} words. 

        Text: ```{_txt_to_be_summarized}```
        """
    else:
        _summarize_prompt = f"""
                Your task is to generate a short summary of a text

                Summarize the text below, delimited by triple 
                backticks. 

                Text: ```{_txt_to_be_summarized}```
                """
        
# This code block is executed when the "Summarize" button is clicked in the "Summarizing" tab of the
# Streamlit app. It retrieves the text to be summarized from a text area input, creates a prompt for
# the OpenAI API to generate a summary, and calls the `get_completion` function to generate the
# summary using the specified OpenAI language model and temperature. The generated summary is then
# displayed in the app using the `st.write` function. If there is an error during the API call, an
# error message is displayed using the `st.error` function.
    if st.button('Summarize'):
        st.divider()
        try:
            with st.spinner('Wait for it...'):
                response = get_completion(_summarize_prompt, _model, _temperature)
                
            st.success('Done!')
            st.write(response)
            
        except Exception as e:
            st.error(f'This is an error : {e}', icon="🚨")

# ========================================[Summarizing TAB]===============================================================================


# ========================================[Inferring TAB]==================================================================================
with tab2:
   st.header("Inferring")
   st.write("Use Chat Gpt for sentiment analisys.")
   st.divider()

   _txt_inferring = st.text_area('Text to be analized : ', '')

   _inferring_prompt = f"""
                        What is the sentiment of the following text,
                        which is delimited with triple backticks?

                        text: '''{_txt_inferring}'''
                        """
   _emotions_prompt = f"""
                        Identify a list of emotions that the writer of the 
                        following text is expressing. Include no more than 
                        five items in the list. 

                        Format your response as a list of enumerated items with new line format for every item

                        text: '''{_txt_inferring}'''
                        """
   _identify_emotions = st.checkbox("Get emotions of the text")
    
   emotions = None
   if st.button('Inferring'):
        st.divider()
        try:
            with st.spinner('Wait for it...'):
                response = get_completion(_inferring_prompt, _model, _temperature)
                if _identify_emotions is True:
                    emotions = get_completion(_emotions_prompt, _model, _temperature)

            st.success('Done!')
            st.write(response)
            if emotions is not None:
                st.subheader("Emotions in the text : ")
                st.write(emotions)
            
        except Exception as e:
            st.error(f'This is an error : {e}', icon="🚨")


# ========================================[Inferring TAB]==================================================================================


# ========================================[Transforming TAB]==================================================================================

with tab3:
   st.header("Transforming")
   st.write("Use Chat Gpt for translation, spelling and grammar checking, tone adjustment, and format conversion.")
   st.divider()

   # `input_column, output_column = st.columns(2)` is creating two columns in the Streamlit app
   # interface and assigning them to the variables `input_column` and `output_column`. This allows for
   # side-by-side display of content or widgets in the app. The `2` parameter specifies that there
   # should be two columns.
   st.subheader("Translation")
   input_column, output_column = st.columns(2)

   with input_column:
    _txt_translating = st.text_area('Text to be translated : ', '')
    _languages = ["Spanish", "English", "Korean"]
    _language_selection = st.selectbox("Languages:", options=_languages)
    _translating_prompt = f"""
                        Translate the following text to {_language_selection},
                            which is delimited with triple backticks?

                            text: '''{_txt_translating}'''
                            """
    if st.button("Translate"):
            try:
                with st.spinner('Wait for it...'):
                    response = get_completion(_translating_prompt, _model, _temperature)

                st.success('Done!')
                with output_column:
                    st.text_area('Text translated : ', response)
                
            except Exception as e:
                st.error(f'This is an error : {e}', icon="🚨")

       
   st.subheader("Tone transformation")
   tone_col_in, tone_col_out = st.columns(2)
   with tone_col_in:
        _txt_translating_tone = st.text_area('Input text : ', '')

        _tones = ["Business letter", "Casual", "Formal", "Teewt", "Facebook Post"]

        _language_selection_tone = st.selectbox("Tones :", options=_tones)
        _translating_tone_prompt = f"""
                            Translate the following text to a {_language_selection_tone},
                            which is delimited with triple backticks?

                            text: '''{_txt_translating_tone}'''
                            """
        if st.button("Translate tone"):
                try:
                    with st.spinner('Wait for it...'):
                        response = get_completion(_translating_tone_prompt, _model, _temperature)

                    st.success('Done!')
                    with tone_col_out:
                        st.text_area('Text translated : ', response)
                    
                except Exception as e:
                    st.error(f'This is an error : {e}', icon="🚨")

       
# ========================================[Transforming TAB]==================================================================================
