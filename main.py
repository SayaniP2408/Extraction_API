# app/main.py

from fastapi import FastAPI
from routes.website import router as website_router

app = FastAPI(
    title="Website Detail Extractor",
    description="This API scrapes the homepage of a website and provides details like industry, company size, and location.",
    version="1.0.0",
)

# Include the website extraction routes
app.include_router(website_router)
