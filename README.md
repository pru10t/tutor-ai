# AI Educational Assistant

An intelligent educational assistant powered by NPU-accelerated AI, built with Streamlit. This application helps teachers and students by providing personalized educational content, curriculum generation, and interactive learning experiences.


## Features

- 🎯 Multiple Teaching Modes (Learn Concept, Practice Questions, Get Explanation)
- 📚 Curriculum Generation with PDF Export
- 🎨 Support for Multiple Teaching Styles
- 🌍 Multi-language Support
- 📑 PDF Document Processing
- 💻 NPU Acceleration Support


## Authors
- **Pruthvi Taranath**  
  Contact: pt256@nyu.edu
  
- **Nirmal Boghara**  
  Contact: nb3964@nyu.edu 

## Requirements

- Python 3.8+
- Streamlit
- ONNX Runtime
- Other dependencies (see requirements.txt)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tutor-ai.git
cd tutor-ai/src
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```


4. Once this is successful, the application is up and running on 

```bash
Local URL: http://localhost:8501
Network URL: http://10.18.222.37:8501
```



## Usage (Prompts)

1. Select teaching styles and set learning parameters
2. Upload curriculum documents (optional)
3. Set learning objectives
4. Choose the teaching mode
5. Enter your question or topic
6. Get AI-generated responses

## Testing Instructions

1. Try running : pytests tests/      (If this doesnt work, proceed with below steps)
2. cd tests
3. pytest test_health_check.py    (Tests if the app is running on localhost)
4. pytest test_model_handler.py    (Tests if Local LLM is up and running)


## License

[MIT License](LICENSE)
