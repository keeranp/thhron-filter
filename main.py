from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import io
from starlette.responses import StreamingResponse

from gen import generate

app = FastAPI()

@app.get('/')
def root():
    return {"Hello": "LL"}

@app.post('/filter/thorn')
async def thorn(file: UploadFile = File(...)):
    content = await file.read()

    #Process image
    nparr = np.fromstring(content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    new_img = generate(img)

    _, encoded_img= cv2.imencode(".png",new_img)

    return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/png")