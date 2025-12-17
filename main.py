import os
import shutil
import time
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from services.analyzer import analyze_video
from data_models.CreativeAdsAnalysis import CreativeAnalysis
load_dotenv()

app = FastAPI(title="Video Analysis Agent (Gemini Native)")


@app.post("/analyze", response_model=CreativeAnalysis)
async def analyze_endpoint(file: UploadFile = File(...)):
    # save temp file
    temp_filename = f"temp_{file.filename}"
    try:
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        #analyze video
        result = analyze_video(temp_filename)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # cleanup temp file    
    finally: 
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)