import os
from dotenv import load_dotenv
from utils.pdf_extractor import extract_text_from_pdf
from utils.indexer import create_index_from_text
from utils.confidence_measure import is_low_confidence
from ui_components import setup_sidebar_and_title, upload_pdf_ui, ask_question_ui, display_json_response, stop_search_ui, new_pdf_upload_ui, display_message
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAIChat,OpenAI
import json
import logging

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
chain = load_qa_chain(OpenAIChat(model_name='gpt-3.5-turbo', temperature=0.0), chain_type="stuff")


logging.basicConfig(level=logging.INFO)


def process_question(question, docsearch):
    try:
        docs = docsearch.similarity_search(question)
        answer = chain.run(input_documents=docs, question=question)
        if answer is None or answer.strip() == "" or is_low_confidence(answer):
            return "Data Not Available"
        return answer
    except Exception as e:
        logging.error(f"Error processing question: {e}")
        return "Data Not Available"

def generate_json_response(questions_answers):
    return json.dumps(questions_answers, indent=2)

def handle_question(docsearch):
    query = ask_question_ui()
    if query:
        answer = process_question(query, docsearch)
        questions_answers = {query: answer}
        response_json = generate_json_response(questions_answers)
        display_json_response(response_json)

if __name__ == "__main__":
    setup_sidebar_and_title()
    pdf = upload_pdf_ui()

    if pdf:
        raw_text = extract_text_from_pdf(pdf)
        docsearch = create_index_from_text(raw_text)
        query = ask_question_ui()

        if query:
            answer = process_question(query, docsearch)
            questions_answers = {query: answer}
            response_json = generate_json_response(questions_answers)
            display_json_response(response_json)