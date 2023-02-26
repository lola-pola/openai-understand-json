from io import StringIO 
import streamlit as st
import openai
import json
import os


# Set up API key
openai.api_key=st.text_input('here you need need to put azure open ai key')


def json_cutter(filename,split_length):
    json_str = str(filename)
    sub_strings = [json_str[i:i+split_length] for i in range(0, len(json_str), split_length)]
    master_list = []
    with st.spinner('cutting data'):
        for sub in sub_strings:
            sub_list = list(sub)
            master_list.append(sub_list)
    return master_list




def sendin_to_gpt(text_data ,data,model):
    response = openai.Completion.create(
        engine=model,
        prompt=text_data + data,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    keywords = response.choices[0].text
    return keywords.strip().split("\n")



data =None

filename = st.file_uploader("Upload json file to use in GPT ", type=["json"])


## main params
split_length = 4000
text_data = "sending you json: "

if filename is not None:
    filename = filename.getvalue()
    if st.checkbox('show file'):
        st.write(json.loads(filename))
    if st.checkbox('start coverting file'):
        chr_list = json_cutter(filename=json.loads(filename),split_length=split_length)
        if chr_list:
            model = st.selectbox('model',("text-davinci-002","text-davinci-003"))
            if st.checkbox('start sendign to open ai'):
                for chr in chr_list:
                    # print(len(chr_list))
                    _chr = ''.join(chr)
                    if chr == chr_list[0]:
                        text_data=text_data
                        data = sendin_to_gpt(text_data,data=_chr,model=model)
                    elif chr == chr_list[-1]:
                        data = 'this is the end of the json'
                        text_data = _chr
                        data = sendin_to_gpt(text_data,data=data,model=model)
                    else:
                        text_data=''
                        data = sendin_to_gpt(text_data,data=_chr,model=model)
                        
print('wellcom to data explain')
if data is not None:
    q_models = st.selectbox('models to use',("text-davinci-002","text-davinci-003"))
    question = st.text_input('ask a question')
    if question != '':
        st.write(sendin_to_gpt(text_data=question,data='in json that i sent ',model=q_models))



