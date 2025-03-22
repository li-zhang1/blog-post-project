from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwtToken import SECRET_KEY, ALGORITHM, verifyToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(appToken: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
  return verifyToken(appToken,credentials_exception)