from fastapi import FastAPI
from pydantic import BaseModel
from detector import analyze_url
from fastapi.middleware.cors import CORSMiddleware

# Built with FastAPI because I have zero patience for Flask boilerplate today
# Built with FastAPI because I have zero patience for Flask boilerplate today
app = FastAPI(title="PhishGuard AI API")

# Allow all CORS because dealing with browser security blocks on localhost is torture
# Allow all CORS because dealing with browser security blocks on localhost is torture
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str
    has_login_form: bool = False
    has_cross_site_action: bool = False

@app.post("/api/analyze")
async def analyze(request: URLRequest):
    result = analyze_url(request.url, request.has_login_form, request.has_cross_site_action)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
