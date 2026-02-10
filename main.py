import serial, base64
from fastapi import FastAPI
from uvicorn import run
from pyfingerprint.pyfingerprint import PyFingerprint

app = FastAPI()

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
            return {"template": base64.b64encode(template2byte).decode("utf-8")}

        return {"error": "No finger detected"}
    
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
