from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def health_check_root():
    return {"status": "OK", "message": "Healthcheck root is healthy!"}


@app.get("/details")
def health_check_details():
    return {"status": "OK", "version": "1.0.0"}
