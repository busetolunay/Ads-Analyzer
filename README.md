# 🎬 AI Video Creative Analyzer

**Automated performance tagging for mobile game ad creatives using Multimodal LLMs.**

## 📌 Executive Summary

The mobile gaming industry relies on high-velocity creative iteration, often producing hundreds of ad variations to test user engagement. This project solves the **"Creative Intelligence"** bottleneck: the inability of human teams to manually label the sheer volume of assets produced under stringent time constraints.

I developed this tool as an automated pipeline to classify video creatives with high-level semantic metadata—specifically detecting **"Fail" concepts**, **Gameplay Core**, and **Voice Over (VO) demographics**.

I containerized the solution with **Docker** for reproducibility, supporting two modes of operation:
1.  **Batch Processor:** Scans a local folder of videos and generates a comprehensive CSV report.
2.  **API Service:** A FastAPI endpoint for real-time analysis integration.

---

## 🏗️ Architectural Blueprint & Methodology

To determine the optimal solution, I evaluated three primary architectural patterns for video understanding. I ultimately rejected traditional pipelines in favor of a **Native Multimodal LLM** approach.

##### 1. Traditional Computer Vision + Audio Analysis  (OpenCV + OCR) 
The classical ML engineering method builds a modular pipeline of specialized, narrow libraries (e.g., OpenCV for frames, Tesseract for OCR, Librosa for audio).
* **Critique:** I found this approach to be **outdated and semantically inadequate**. Hard-coding color thresholds for "Gameplay" fails if a developer changes the UI color scheme. OCR can read the word "FAIL," but lacks the narrative context to understand if the video is actually a "Fail Ad" or just contains the text.
* **Verdict:** Insufficiently robust for semantic nuances.

##### 2. Frame-Extraction + VLMs + Audio Analysis (GPT-4o)
This approach treats video as a sequence of static images (e.g., 1 frame per second) sent to a Vision model.
* **Critique:** This introduces a **Modality Gap**. Separating audio and video breaks the semantic link—if a character screams "No!" exactly when they fall, the "Fail" concept is reinforced. Processing these separately loses that synchronization. Furthermore, the unit economics are prohibitive (~$5.00/1M tokens) for high-volume ad tech use cases.
* **Verdict:** Suboptimal due to high latency and cost.

##### 3. The Selected Solution: Native Multimodal (Gemini 2.5 Flash)
I chose to implement Google’s Gemini 2.5 Flash because it is designed as a "native" multimodal model. It does not merely "see" images; it is trained on interleaved sequences of audio, video, and text tokens.
* **Native Audio Understanding:** It processes audio waveforms directly, allowing it to detect tone and speaker gender without intermediate speech-to-text steps.
* **Long Context Window:** It watches the entire video stream, maintaining temporal continuity required to understand the narrative arc of a "Fail" ad.
* **Cost Efficiency:** It offers a  cost reduction compared to competing frontier models.

### 📊 Comparative Technology Review

| Feature | OpenCV / Tesseract (Traditional) | GPT-4o (Frame Extraction) | Gemini 2.5 Flash (Native MLLM) |
| :--- | :--- | :--- | :--- |
| **Setup Complexity** | High ,Multiple libraries | Medium (Image processing logic) | Low  |
| **Semantic Reasoning** | Very Low (Rule-based) | Very High | High  |
| **Audio Integration** | Complex ,Separate DSP pipeline | Disconnected (Text-based) | Native / Seamless |
| **Cost Profile** | Negligible (Compute only) | High  | Low  |
| **Fail Detection** | Poor (Misses context) | Excellent | Good |

---

## 🛠️ Implementation Details

### Structured Data Enforcement
I utilized **Pydantic** models to define the output schema strictly.
> **Benefit:** This forces the LLM to return valid JSON matching my defined schema. It prevents "hallucinated" formats and ensures the final CSV is always clean and ready for data analysis.

### "Code-Data Decoupling" with Docker
I designed the Docker architecture to be stateless.
**Strategy:** Videos are not baked into the image. I use Docker Volume mapping to mount the local video folder into the container at runtime. This allows the tool to process 10 or 10,000 videos without rebuilding the image.

---
 ## Repository Structure
```bash
/
├── data_models/             # Pydantic schemas for data validation
│   └── CreativeAnalysis.py  
├── services/                # Shared business logic (LLM abstraction)
│   └── llm_analyzer.py      
├── videos/                  # Default input folder for testing
├── .env.example             # Configuration template
├── batch_runner.py          # Script for bulk CSV generation
├── docker-compose.yml       # Orchestration for Batch & API services
├── Dockerfile               # Container definition
├── main.py                  # FastAPI entry point
├── README.md                # Documentation
└── requirements.txt         # Python dependencies
```

## 🚀Deployment & Quick Start

### Prerequisites
* Docker Desktop installed and running.
* A Google Gemini API Key (Free tier is sufficient).

### 1. Configuration

This project separates Code from Data using Environment Variables. You do not need to move your videos into the project folder; you can point the container to them.
Clone the repository:

```bash
git clone [<your-repo-url>](https://github.com/busetolunay/Ads-Analyzer.git)
cd [<your-repo-name>](https://github.com/busetolunay/Ads-Analyzer.git)
```

Setup Environment: Create a .env file in the root directory .
```Ini, TOML

# 1. AI Provider Key (Required)
GOOGLE_API_KEY=your_gemini_api_key_here

# 2. Input/Output Paths for Docker
# Point this to the folder on YOUR machine containing .mp4 files
HOST_VIDEO_FOLDER=./videos

# Point this to where you want the CSV report saved
HOST_OUTPUT_FOLDER=./results
Create a `.env` file in the root directory (or rename `.env.example`).
```

##### Method 1: Docker Compose (Recommended)
This method ensures the application runs exactly as intended, regardless of your local Python environment.

To Run the Batch Analysis (Generate CSV): This starts the container, mounts your video folder, processes the files, saves the CSV, and shuts down.

```bash
docker-compose up batch-analyzer
```

Outcome: Check your defined HOST_OUTPUT_FOLDER for final_analysis_results.csv.

To Run the API Server: This starts a persistent server for real-time testing.

```bash
docker-compose up api-server
```
Outcome: Access the Swagger UI at http://localhost:8000/docs.

##### Method 2: Local Python Execution
Useful for development or debugging.

```bash
# Install dependencies
pip install -r requirements.txt
# Run Batch Script
python batch_runner.py
# Run API Server
uvicorn main:app --reload
```

## Future Improvements
While the current solution provides a solid baseline for static tagging, the next phase of development would focus on Deep Content Intelligence and Market Awareness.

#### 1. Granular Temporal Analysis (Timestamping)
Current State: The model provides a global summary 

Improvement: Implement frame-perfect event logging to generate a timeline JSON.

Example: {"00:02": "Character_Death", "00:05": "Character_Appear", "00:08": "Logo_Reveal"}.

Business Value: Allows the marketing team to correlate exact moments in the video with user drop-off rates (retention analysis).

2. Character & Asset Tracking
Improvement: Fine-tune a Vision Transformer (ViT) or use Gemini's object tracking to ID specific game characters across the video duration.

Example: "Character 'Buse' appears at 0:02, 0:04, and 0:10."

Business Value: Identify which characters or skins drive the highest conversion rates in ads.

#### 3. Trend & Audio Intelligence (Web Search Integration)
Improvement: Give the AI agent internet access (via Tool) to cross-reference audio and visual styles against current social media trends.

Workflow:
Extract audio transcript/melody.

Search TikTok/Reels databases.

Output: "Uses trending audio 'Spooky Scary Skeletons' (Trend Peak: Oct 2025)."

Business Value: detect if an ad is using "stale" memes or riding a current viral wave.

#### 4. Agentic Workflows & Multi-Agent Orchestration
Instead of a linear script, the system could evolve into an Autonomous Creative Lab using a framework like LangGraph or CrewAI:

The Researcher Agent: Performs web searches to identify if the audio or visual style is currently trending on TikTok/Reels.

The Critic Agent: Compares the AI-generated tags against the creative_metrics.csv. If an ad has a high Click-Through Rate CTR but "boring" tags, the Critic Agent forces a re-analysis to find the hidden factor.

The Iteration Agent: Based on analysis, this agent generates a new script or visual storyboard to improve the ad for the next campaign.

#### 5. Production-Grade Engineering
Asynchronous Processing (Celery/Redis): Decouple video processing from the API response to handle heavy loads without timeouts.

Vector Database (Pinecone/Weaviate): Store video embeddings to enable semantic search (Marketers can query: "Show all ads that look like UGC content" without needing explicit tags).

Golden Dataset Evaluation: Establish a CI/CD pipeline that tests the prompt against human-labeled videos to ensure tagging accuracy remains high as the model evolves.

