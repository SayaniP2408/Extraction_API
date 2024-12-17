# app/auth.py

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends
from settings import SECRET_KEY

security = HTTPBearer()

def check_authorization(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    