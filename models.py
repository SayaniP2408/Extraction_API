# app/models.py

from pydantic import BaseModel, Field

class WebsiteRequest(BaseModel):
    url: str = Field(..., description="The URL of the website to scrape.", example="https://example.com")

class WebsiteDetailsResponse(BaseModel):
    industry: str = Field(..., description="Industry the company belongs to.", example="Technology")
    company_size: str = Field(..., description="Size of the company (e.g., small, medium, large).", example="Medium")
    location: str = Field(..., description="Location of the company.", example="San Francisco")
