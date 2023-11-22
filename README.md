## Zania PDF 📑 Chat App💬

### Introduction:

Zania PDF Chat App is a Python-based application designed to provide an interactive way to extract and query information from PDF documents. It leverages LLM's and Langchain framework for answering queries based on the content of the uploaded PDF.

### Demo: https://youtu.be/peyhBucTaxE

### Key Features:

  - PDF Text Extraction: Extracts text from uploaded PDF files for processing.
  - Text Indexing and Search: Creates a searchable index of extracted text for efficient query handling.
  - Question-Answering Capabilities: Utilizes LangChain and OpenAI GPT models to answer questions based on the PDF content.
  - Interactive User Interface: Built with Streamlit, offering an intuitive and user-friendly interface.
  - Error Handling: Robust error handling and logging for stable application performance.
  - Modular Design: Cleanly structured code for easy maintenance and scalability.

### File Structure:

The application is organized into several modules, each with a specific responsibility:

    Zania-PDF-Chat-App/
    │
    ├── main.py                    # Main application script; handles Streamlit UI and app flow
    │
    ├── utils/                     # Utility scripts for various functionalities
    │   ├── pdf_extractor.py       # Extracts text from PDF files
    │   ├── indexer.py             # Creates searchable index from extracted text
    │   └── confidence_measure.py  # Logic for determining low-confidence answers
    │
    ├── ui_components.py           # Functions for Streamlit UI components
    │
    ├── test_app.py                # Unit tests for validating components
    │
    └── .env                       # (Not in repository) Environment variables like OpenAI API key

### Module Responsibilities:

   - pdf_extractor.py
 ```
  Purpose: Extracts text from a given PDF file.

  Implementation: Utilizes PyPDF2.PdfReader for reading PDF files.

  Function extract_text_from_pdf:

       - Reads each page of the PDF and extracts text.

       - Concatenates text from all pages, separated by newline characters.

       - Exception handling to log errors during PDF processing.

  Reason for Choice: PyPDF2 is a robust and widely-used library for handling PDF files in Python. It provides reliable mechanisms for reading and extracting text.
 ```
  
  - indexer.py:
```
  Purpose: Creates a searchable index from the extracted text.

  Implementation:

      CharacterTextSplitter from langchain.text_splitter:

          - Splits the text into chunks based on character count.

          - chunk_size=1000 and chunk_overlap=200 are configured to balance between manageable chunk sizes and contextual overlap for better search accuracy.
          separator="\n" ensures that the split happens at line breaks, preserving the readability of text.

      OpenAI Embeddings:

          Converts text chunks into vector embeddings using OpenAI's language models.

      FAISS (Facebook AI Similarity Search):

          Efficiently indexes these embeddings for fast similarity searching.

  Reason for Choice:

       - CharacterTextSplitter effectively manages large text documents by breaking them into smaller, searchable segments.

       - OpenAI Embeddings provide high-quality, context-rich vector representations of text.

       - FAISS is renowned for its efficiency in similarity search and indexing, making it an ideal choice for searching within large volumes of text.

```

  - ui_components.py:
     ```
     Purpose: Manages all user interface components for the Streamlit app.

    Implementation:
     
        Functions to create and handle UI elements like file uploader, text input, buttons, and displaying responses.
     
    Reason for Choice:
     
        Separating UI components into a distinct module follows the principle of modularity, making the codebase more organized and maintainable.
     ```
     
    - main.py:
    ```
     Purpose: Main application script that integrates all modules and runs the application using Streamlit.

    Implementation:
    
        - Sets up the Streamlit UI using functions from ui_components.py.
    
        - Manages the workflow of uploading PDFs, extracting text, indexing, and querying.
    
        process_question Function:
    
             - Searches the indexed text for answers to user queries.
             - Includes a check for low-confidence answers using is_low_confidence.
             - temperature=0.0 in OpenAIChat is set to reduce randomness in responses, aiming for more direct and precise answers.
    
        Error Handling:
    
             - Robust error handling for issues during question processing, with user-friendly error messages.
    
    Reason for Choice:
    
         - Streamlit offers a straightforward way to create interactive web applications for Python scripts.
    
         - The decision to use temperature=0.0 is to prioritize deterministic responses from the model, which is suitable for a fact-based Q&A context.
        
    ```

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
