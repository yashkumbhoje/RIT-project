from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="VSpireInnovations Website API",
    description="Backend API for VSpireInnovations company website",
    version="1.0.0"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home page
@app.get("/")
def home():
    return FileResponse("frontend/index.html")


# Health check endpoint
@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "message": "VSpireInnovations backend is running"
    }


# Company information API
@app.get("/api/company")
def company_info():
    return {
        "name": "VSpireInnovations",
        "tagline": "We Vision Inspiration",
        "services": [
            "Artificial Intelligence",
            "Data Science",
            "DevOps",
            "MLOps",
            "Full Stack Development"
        ]
    }