import streamlit as st
from nanonets import NANONETSOCR
import tempfile

def process_file(uploaded_file):
    model = NANONETSOCR()
    model.set_token('95e09787-0a63-11ee-9c73-1e85f057e35b')
    pred_json = model.convert_to_prediction(uploaded_file.name)
    value1 = pred_json['results'][0]['page_data'][0]['words']
    extracted_text = []
    for item in value1:
        if 'text' in item:
                extracted_text.append({'key': item['text']})

    print(extracted_text)

    value = pred_json['results'][0]['page_data'][0]['raw_text']
    print(value)
    return extracted_text, value
    


st.title('PDF to JSON Converter')

uploaded_file = st.file_uploader("Choose a file", type='pdf')
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)
    result = process_file(uploaded_file)
    st.write(result)
    

    # def generate_text():
    #     content_string = " ".join(result)
    #     temp_file = tempfile.NamedTemporaryFile(delete=False)
    #     temp_file.write(string_list.encode())
    #     temp_file.close()
    #     return temp_file.name
    
    # file_path = generate_text()

    # st.download_button("Download Text File", file_path, file_name="output.txt")