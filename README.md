# OpenAI Understand JSON

[![GitHub license](https://img.shields.io/github/license/lola-pola/openai-understand-json.svg)](https://github.com/lola-pola/openai-understand-json/blob/main/LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/lola-pola/openai-understand-json/main/app.py)

A Streamlit application that allows users to upload a JSON file, sends it to OpenAI, and then lets users ask questions about it.

## Requirements

* Python 3.10+
* An OpenAI API key

## Installation

1. Clone the repository:
```
git clone https://github.com/lola-pola/openai-understand-json.git
cd openai-understand-json
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. run streamlit 
```
streamlit run app/app.py
```



## Usage

1. Set your OpenAI API key by running the app and entering your API key in the text input field.

2. Upload a JSON file by clicking the "Upload json file to use in GPT" button.

3. If you want to see the contents of the file, click the "show file" checkbox.

4. If the file is too large to process in one request to OpenAI, it will be split into smaller chunks. You can adjust the `split_length` parameter in the `json_cutter` function to control the chunk size.

5. Once the file has been split, select an OpenAI language model from the dropdown menu, and click the "start sending to OpenAI" checkbox to send each chunk of the file to OpenAI. The results of each request will be stored in the `data` variable.

6. After the entire file has been sent to OpenAI, you can use the "models to use" dropdown menu to select a language model to use for answering questions about the JSON file.

7. Type your question into the "ask a question" text input field, and click the "Submit" button to send your question to OpenAI. The results of the request will be displayed in the Streamlit app.


4. Run the following command to start the container:
```
docker build . -f openai-understand-json:1
docker run -p 8501:8501 openai-understand-json:1
```

5. Open your web browser and navigate to http://localhost:8501 to access the Streamlit app.

## Acknowledgements

This project was inspired by [Streamlit + OpenAI GPT-3: Creating a Custom Question Answering App](https://towardsdatascience.com/streamlit-openai-gpt-3-creating-a-custom-question-answering-app-1f5b408e57d5) by Akshay Gupta.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.





## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.