# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
import uvicorn

app = FastAPI()

# Allow frontend requests
origins = ["https://novusolutions.netlify.app/"]  # Change to your frontend URL in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define root route
@app.get("/")
def home():
    return {"message": "Welcome to Novu Solutions API!"}

# Include authentication router
app.include_router(auth_router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
