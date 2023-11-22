## Zania PDF 📑 Chat App💬

### Introduction

Zania PDF Chat App is a Python-based application designed to provide an interactive way to extract and query information from PDF documents. It leverages LLM's and Langchain framework for answering queries based on the content of the uploaded PDF.

### Demo: https://youtu.be/peyhBucTaxE

### Key Features

  - PDF Text Extraction: Extracts text from uploaded PDF files for processing.
  - Text Indexing and Search: Creates a searchable index of extracted text for efficient query handling.
  - Question-Answering Capabilities: Utilizes LangChain and OpenAI GPT models to answer questions based on the PDF content.
  - Interactive User Interface: Built with Streamlit, offering an intuitive and user-friendly interface.
  - Error Handling: Robust error handling and logging for stable application performance.
  - Modular Design: Cleanly structured code for easy maintenance and scalability.

### File Structure

The application is organized into several modules, each with a specific responsibility:

     - main.py: The main script that runs the application, handles the Streamlit UI, and orchestrates the flow of the application.
     
     - utils/pdf_extractor.py: Handles the extraction of text from PDF files.
     
     - utils/indexer.py: Manages the indexing of extracted text for search and retrieval.
     
     - utils/confidence_measure.py: Mange and maintail logic for Checking for phrases that might indicate uncertainty
     
     - ui_components.py: Contains functions related to the Streamlit user interface components.

     - test_app.py: holds unit test function to validate the components
     
     - .env: (Not in the repository) A file for storing environment variables like the OpenAI API key.```

### Module Responsibilities

    - pdf_extractor.py:
        Extracts text from a given PDF file.
        Returns the extracted text as a string.
    - indexer.py:
        Splits the extracted text into manageable chunks.
        Creates a searchable index using LangChain and FAISS.
    - ui_components.py:
        Houses functions for creating and managing UI components like buttons, text inputs, and displaying responses.
    - main.py:
        Initializes the application.
        Manages the workflow of uploading PDFs, extracting text, indexing, querying, and displaying results.

### Steps to Run and Execute the Code

  #### 1. Clone the Repository:



  ```
  git clone https://github.com/your-username/zania-pdf-chat-app.git
  cd zania-pdf-chat-app
```

#### 2. Set Up a Python Environment:

   It's recommended to use a virtual environment:
   ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

#### 3. Install Dependencies:

  Ensure requirements.txt is present and run:

   ```
    pip install -r requirements.txt
   ```

#### 4. Environment Variables:

   - Create a .env file in the root directory.
   - Add your OpenAI API key:
```
    makefile

    OPENAI_API_KEY=your_openai_api_key_here
  ```  

#### 5. Running the Application:

  Execute the main script with Streamlit:

  ```
  streamlit run main.py
```

  Using the Application:
      The Streamlit interface should open in your browser.
      Upload a PDF file and ask questions to interact with the application.

### Conclusion

Zania PDF Chat App demonstrates the power of LLM techniques with user-friendly interfaces. It serves as a useful tool for extracting and interacting with information from PDF documents, showcasing the potential of AI in information retrieval and processing.
