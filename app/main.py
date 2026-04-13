from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 静的ファイル（CSSなど）のルーティング
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# テンプレートディレクトリ
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Web App"})
