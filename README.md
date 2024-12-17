# Website Detail Extractor API

This FastAPI application scrapes the homepage of a website and extracts specific details about the company such as the industry, company size, and location. The extracted information is returned in a structured format using Pydantic models.

## Project Structure

/fastapi_project │ ├── app/ │ ├── init.py │ ├── main.py # The entry point of your FastAPI application │ ├── models.py # Pydantic models for request and response │ ├── auth.py # Authentication and authorization handling │ ├── utils.py # Utility functions (like the AI model integration) │ ├── routes/ │ │ └── website.py # The route for the /extract-details endpoint │ └── settings.py # App settings (like the secret key) │ └── requirements.txt # Dependencies for the project

bash
Copy code

## Setup Instructions

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/SayaniP2408/Extraction_API.git
cd Extraction_API
2. Create a Virtual Environment (Optional but recommended)
Create a virtual environment to keep the dependencies isolated:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the dependencies
Install all the required dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
You can also install the dependencies manually by running:

bash
Copy code
pip install fastapi uvicorn httpx beautifulsoup4 transformers pydantic
4. Configure the Secret Key
The API requires an Authorization header with a secret key for access. You can set the secret key in app/settings.py:

python
Copy code
SECRET_KEY = "your-secret-key"  # Replace with your actual secret key
Make sure to replace "your-secret-key" with a strong secret key of your choice.

5. Run the FastAPI Application
To start the FastAPI application, run the following command:

bash
Copy code
uvicorn app.main:app --reload
This will start the server at http://127.0.0.1:8000.

6. Access Swagger UI
Once the FastAPI application is running, you can access the interactive API documentation at:

arduino
Copy code
http://127.0.0.1:8000/docs
In the Swagger UI, you'll see an Authorize button in the top-right corner. Click on it and enter the following authorization header:

vbnet
Copy code
Bearer your-secret-key
Replace your-secret-key with the actual secret key you configured in app/settings.py.

7. Make API Requests
After authorizing, you can interact with the /extract-details endpoint. Here's how:

Click Try it out for the /extract-details endpoint.
In the request body, enter the JSON object with the URL of the website you want to scrape. For example:
json
Copy code
{
  "url": "https://example.com"
}
Click Execute.
The API will return a response with the extracted details, such as:

json
Copy code
{
  "industry": "Technology",
  "company_size": "Medium",
  "location": "San Francisco"
}
8. Example Response
After executing a request, the API will return a JSON response similar to:

json
Copy code
{
  "industry": "Technology",
  "company_size": "Medium",
  "location": "San Francisco"
}
The response includes the following fields:

industry: The industry the company belongs to.
company_size: The size of the company (small, medium, large).
location: The company's location.
Endpoints
POST /extract-details
This endpoint accepts a POST request with the following body:

json
Copy code
{
  "url": "https://example.com"
}
It returns a 200 OK response with the company details, including the industry, company size, and location.

Authorization Header: The request must include a valid Bearer token in the header:

vbnet
Copy code
Authorization: Bearer your-secret-key
Project Files
app/main.py: Entry point for the FastAPI application, where the app instance is created.
app/models.py: Defines Pydantic models for request and response.
app/auth.py: Handles the authentication logic (authorization header validation).
app/utils.py: Contains utility functions, including scraping logic and AI-based question answering.
app/routes/website.py: Contains the logic for the /extract-details endpoint.
app/settings.py: Holds the application's configuration, including the secret key for authentication.
Deployment
To deploy this app, you can use a platform like Render, Railway, or Fly.io. These platforms allow you to easily deploy FastAPI applications for free or at a minimal cost.

Example Deployment on Render
Create a new Web Service on Render.
Connect your GitHub repository.
Set the build command to pip install -r requirements.txt.
Set the start command to uvicorn app.main:app --host 0.0.0.0 --port 80.
Set the environment variable for the secret key:
Key: SECRET_KEY
Value: your-secret-key
Once deployed, Render will provide you with a public URL where you can access the API.

Contributing
Feel free to open issues or submit pull requests for improvements or fixes.
