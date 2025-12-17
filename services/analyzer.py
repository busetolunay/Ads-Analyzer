import os
import time
from dotenv import load_dotenv
from google import genai 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from data_models.CreativeAdsAnalysis import CreativeAnalysis

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# Gemini 2.5 pro or flash , native Multimodal"
# gemini-2.5-flash is faster/cheaper but less capable than "gemini-1.5-pro"
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0
)

def analyze_video(video_path: str) -> CreativeAnalysis:
    """analyze a video file using Gemini's native video understanding capabilities.
    """
    print(f"1. Uploading {video_path} to Google AI Studio...")
    
    # upload via Native SDK is required for videos over 20mb
    video_file = client.files.upload(file=video_path)
    print(f"   Uploaded: {video_file.name}")

    # videos require a processing phase before they can be analyzed
    print("2. Waiting for video processing (this may take a moment)...")
    while video_file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        video_file = client.files.get(name=video_file.name)

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
