from fastapi import FastAPI

from urls.auth import auth

app = FastAPI()

app.include_router(auth)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8012, reload=True)
