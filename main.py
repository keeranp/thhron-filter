from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import io
import base64
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from gen import generate

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/filter/thorn')
async def thorn(file: UploadFile = File(...)):
    print(file.filename)
    content = await file.read()

    #Process image
    nparr = np.fromstring(content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    new_img = generate(img)

    _, encoded_img= cv2.imencode(".png",new_img)

    encoded_img = base64.b64encode(encoded_img)

    return encoded_img