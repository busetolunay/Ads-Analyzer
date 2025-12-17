import os
import shutil
import time
from dotenv import load_dotenv
load_dotenv()

if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
    del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    
from fastapi import FastAPI, UploadFile, File, HTTPException
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from data_models.CreativeAdsAnalysis import CreativeAnalysis
import google.generativeai as genai


if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

# Gemini 1.5 pro or flash , native Multimodal"
# gemini-1.5-flash is faster/cheaper but less capable than "gemini-1.5-pro"
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0
)


def analyze_video(video_path: str):
    """analyze a video file using Gemini's native video understanding capabilities.
    """
    print(f"1. Uploading {video_path} to Google AI Studio...")
    
    # upload via Native SDK is required for videos over 20mb
    video_file = genai.upload_file(path=video_path)
    print(f"   Uploaded: {video_file.name}")

    # videos require a processing phase before they can be analyzed
    print("2. Waiting for video processing (this may take a moment)...")
    while video_file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError("Video processing failed on Google's side.")
    
    print("\n   Video is ready.")
    
    # file_uri and mime_type are required for video media messages
    message = HumanMessage(
        content=[
            {
                "type": "text", 
                "text": "Analyze this mobile game ad. Focus on the narrative flow, how the audio matches the visuals, and the 'hook' in the first 3 seconds."
            },
            {
                "type": "media", 
                "file_uri": video_file.uri,      
                "mime_type": video_file.mime_type 
            }
        ]
    )

    # for structured output
    structured_llm = llm.with_structured_output(CreativeAnalysis)
    
    print("Sending to Gemini 1.5 Pro...")
    try:
        # Gemini takes a moment to "process" the video tokens
        analysis_result = structured_llm.invoke([message])
        return analysis_result
    except Exception as e:
        print(f"Error: {e}")
        raise e


if __name__ == "__main__":
    video_file = "9x16_DayByDay2.mp4" 
    
    if os.path.exists(video_file):
        result = analyze_video(video_file)
        
        print("\n result")
        # .model_dump_json() prints the Pydantic object as a clean JSON string
        print(result.model_dump_json(indent=2))
    else:
        print(f"File not found: {video_file}")