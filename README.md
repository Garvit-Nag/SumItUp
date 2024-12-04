# SumItUp - Intelligent Document Summarization Tool

## Project Overview
SumItUp is a Streamlit-based web application that provides intelligent document summarization and sentiment analysis. Users can either paste text directly or upload documents (PDF, DOCX, TXT) to get concise summaries and understand the emotional tone of the content.

## Features
- Text input via direct paste or file upload
- Supports multiple file formats: TXT, PDF, DOCX
- Customizable summary length
- Sentiment analysis with polarity and subjectivity scores
- User-friendly Streamlit interface

## Prerequisites
- Python 3.12
- pip
- Virtual environment support

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sumitup.git
cd sumitup
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
- On Windows:
  ```bash
  .\venv\Scripts\Activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
streamlit run app.py
```

## Project Structure
```
sumitup/
│
├── app.py                  # Main Streamlit application
│
├── src/
│   ├── __init__.py         # Package initializer
│   ├── document_processor.py  # Document text extraction logic
│   └── summarizer.py       # Text summarization and sentiment analysis
│
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Technologies Used
- Streamlit
- Transformers (Hugging Face)
- TextBlob
- PyPDF2
- python-docx

## Troubleshooting
- Ensure all dependencies are installed
- Check Python version compatibility
- Verify file permissions

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
[Add your license information here]
