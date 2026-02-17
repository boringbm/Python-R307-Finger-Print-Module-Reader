import serial, base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from pyfingerprint.pyfingerprint import PyFingerprint

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/scan")
async def scan_finger():
    try:
        f = PyFingerprint("/dev/ttyUSB0", 57600)
        if f.readImage():
            f.convertImage(1)
            f.createTemplate()
            template = f.downloadCharacteristics(1)
            template2byte = bytes(template)
            return {"status": "success", "message": "Fingerprint Captured", "template": base64.b64encode(template2byte).decode("utf-8")}

        return {"status": "failed", "message": "No finger detected"}

    except Exception as e:
        return {"status": "failed", "message": str(e)}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
