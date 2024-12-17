# app/utils.py

import httpx
from bs4 import BeautifulSoup
from transformers import pipeline
import logging

# AI model pipeline for question-answering using HuggingFace's transformers
qa_pipeline = pipeline("question-answering")

# Set up logging
logger = logging.getLogger(__name__)

async def fetch_website_content(url: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        logger.debug("Successfully fetched website content.")
        return response.text
    except httpx.RequestError as e:
        logger.error(f"Request failed: {e}")
        raise Exception(f"Error fetching the website: {e}")

def parse_html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def extract_entity(text: str, question: str) -> str:
    try:
        result = qa_pipeline(question=question, context=text)
        return result['answer'] if result['answer'] else "Not found"
    except Exception as e:
        return "Error extracting entity"
