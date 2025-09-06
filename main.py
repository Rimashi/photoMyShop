from fastapi import FastAPI, File, UploadFile, Form
import mimetypes
from typing import Annotated
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from photoEditor import Edit, transliterate_filename
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def index():
    print("WORKS")
    return FileResponse("views/index.html")


@app.post('/get/text')
def get_text(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        translit_filename = transliterate_filename(file.filename)
        with open(translit_filename, 'wb+') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    img = Edit(filename=translit_filename)
    return {'text': img.pick_to_text(), "filename": translit_filename}


@app.post("/blur")
def make_blur(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        translit_filename = transliterate_filename(file.filename)
        with open(translit_filename, 'wb+') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    img = Edit(filename=translit_filename)
    extname = img.filename.split(".")[-1]
    filename = "".join(translit_filename.split(".")[0:-1])
    img.blur().save(filename + '_blur.' + extname)
    return {'image': FileResponse('/' + img.filename)}


@app.post("/remove/background")
def remove_background(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        translit_filename = transliterate_filename(file.filename)
        with open(translit_filename, 'wb+') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    img = Edit(filename=translit_filename)
    extname = img.filename.split(".")[-1]
    filename = "".join(translit_filename.split(".")[0:-1])
    img.remove_background().save(filename + '_background.' + extname)
    return {'image': FileResponse('/' + img.filename)}


@app.post("/make/better")
def make_better(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        translit_filename = transliterate_filename(file.filename)
        with open(translit_filename, 'wb+') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    img = Edit(filename=translit_filename)
    extname = img.filename.split(".")[-1]
    filename = "".join(translit_filename.split(".")[0:-1])
    img.universal_filter().save(filename + '_better?.' + extname)

    return {'image': FileResponse('/' + img.filename)}


@app.post("/make/bigger/")
def make_bigger(file: Annotated[UploadFile, Form()], num: Annotated[int, Form()]):
    try:
        contents = file.file.read()
        translit_filename = transliterate_filename(file.filename)
        with open(translit_filename, 'wb+') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    img = Edit(filename=translit_filename)
    print(num)
    extname = img.filename.split(".")[-1]
    filename = "".join(translit_filename.split(".")[0:-1])
    img.make_bigger(num).save(filename + '_bigger' + str(num) + "." + extname)
    return {'image': FileResponse('/' + img.filename)}


@app.get("/download/{filename}")
async def download_file(filename: str):
    return FileResponse(filename, media_type="application/octet-stream", filename=filename)


@app.get("/show/{filename}")
async def show_file(filename: str):
    mime_type, _ = mimetypes.guess_type(filename)
    return FileResponse(path='/' + filename, media_type=mime_type)
