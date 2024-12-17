# app/routes/website.py

from fastapi import APIRouter, Depends, HTTPException
from models import WebsiteRequest, WebsiteDetailsResponse
from auth import check_authorization
from utils import fetch_website_content, parse_html_to_text, extract_entity

router = APIRouter()

@router.post("/extract-details", response_model=WebsiteDetailsResponse)
async def extract_website_details(request: WebsiteRequest, credentials: str = Depends(check_authorization)):
    """
    Scrapes the provided website URL and returns details like industry, company size, and location.
    """
    url = request.url
    try:
        # Fetch the website content
        html_content = await fetch_website_content(url)
        # Parse HTML to get the text
        text = parse_html_to_text(html_content)

        # Extract details using AI model
        industry = extract_entity(text, "What industry does this company belong to?")
        company_size = extract_entity(text, "What is the size of the company?")
        location = extract_entity(text, "Where is the company located?")

        return WebsiteDetailsResponse(industry=industry, company_size=company_size, location=location)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
