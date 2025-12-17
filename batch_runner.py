import os
import glob
import csv
import time
from dotenv import load_dotenv
from services.analyzer import analyze_video
from data_models.CreativeAdsAnalysis import CreativeAnalysis

load_dotenv()

# script trusts that Docker has mounted the data here.
INTERNAL_INPUT_DIR = "/app/data/inputs"
INTERNAL_OUTPUT_DIR = "/app/data/outputs"
OUTPUT_FILENAME = "analysis_results.csv"


def main():
    # ensure output directory exists (good practice)
    os.makedirs(INTERNAL_OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(INTERNAL_OUTPUT_DIR, OUTPUT_FILENAME)
    
    
    # setup output CSV from pydantic model
    field_keys = list(CreativeAnalysis.model_fields.keys())
    fieldnames = ["filename"] + field_keys
    
    #find videos
    videos = glob.glob(os.path.join(INTERNAL_INPUT_DIR, "*.mp4"))
    print(f"Scanning container path: {INTERNAL_INPUT_DIR}")
    print(f"Found {len(videos)} videos to process.")
    if not videos:
        print("No videos found, map the volume correctly in .env file")
        return

    results = []

    for v in videos:
        try:
            # analyze_video returns a CreativeAnalysis object
            analysis_object = analyze_video(v) 
            
            if analysis_object:
                #mode=json ensures Enums are converted to strings instead of python objects
                row_data = analysis_object.model_dump(mode="json")
                
                # CSV handling
                # CSVs can't handle lists like list[str] or list[Enum] 
                # We must join them into a single string.
                for key, value in row_data.items():
                    if isinstance(value, list):
                        row_data[key] = ", ".join(str(x) for x in value)

                row_data["filename"] = os.path.basename(v)
                results.append(row_data)
                print(f"Saved: {os.path.basename(v)}")
            else:
                print(f" Skipped (No result): {os.path.basename(v)}")
                
        except Exception as e:
            print(f"Error processing {os.path.basename(v)}: {e}")
            
        time.sleep(2)# safety pause between videos
        
        
    # 4. Save CSV
    if results:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Done! Results in {output_path}")
    else:
        print("No results generated.")

if __name__ == "__main__":
    main()