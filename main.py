from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(path="/assets", app=StaticFiles(directory="assets"), name="assets")

@app.get("/")
def getroot(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})


@app.get("/blog")
def getDados(request: Request):
        return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/cadastro_cliente")
def getSenha(request: Request):
        return templates.TemplateResponse("cadastro_cliente.html", {"request": request})


@app.get("/cadastro_finalizado")
def getContato(request: Request):
        return templates.TemplateResponse("cadastro_finalizado.html", {"request": request})

@app.get("/cadastro_fornecedor")
def getRestrita(request: Request):
        return templates.TemplateResponse("cadastro_fornecedor.html", {"request": request})

@app.get("/endereco")
def getLogin(request: Request):
        return templates.TemplateResponse("endereco.html", {"request": request})

@app.get("/lojacomcadastro")
def getCriar(request: Request):
        return templates.TemplateResponse("lojacomcadastro.html", {"request": request})

@app.get("/lojasemcadastro")
def getTermos(request: Request):
        return templates.TemplateResponse("lojasemcadastro.html", {"request": request})

@app.get("/opcoes")
def getTermos(request: Request):
        return templates.TemplateResponse("opcoes.html", {"request": request})

@app.get("/sobre")
def getTermos(request: Request):
        return templates.TemplateResponse("sobre.html", {"request": request})

if __name__ == "__main__":
   uvicorn.run(app="main:app", reload=True)