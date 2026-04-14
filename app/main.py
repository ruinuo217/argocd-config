from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"version": "v2.0", "message": "Hello from ArgoCD!"}

@app.get("/health")
def health():
    return {"status": "ok"}
