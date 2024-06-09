from fastapi import FastAPI

from urls.auth import auth

app = FastAPI()

app.include_router(auth)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
