# Quick Recap: Instant Meeting Insights

**Quick Recap: Instant Meeting Insights** is an AI-powered tool that automates meeting summarization using Natural Language Processing (NLP). It extracts key discussion points, decisions, and action items from meeting transcripts or recordings, making meetings more efficient and accessible. The system streamlines communication, reduces manual effort, and enhances productivity in remote and hybrid work environments.

##  Features
- ** Automated Meeting Summarization** – Converts speech to text and generates concise summaries.
- ** Key Points Extraction** – Identifies important discussion topics, decisions, and action items.
- ** Cloud-Based & Scalable** – Designed for seamless processing of small meetings to large conferences.
- ** User-Friendly Interface** – Upload, process, and retrieve summaries through a simple web interface.
- ** API Support** – Integrates with external platforms like Slack, Zoom, and Microsoft Teams.

##  Tech Stack
- **Frontend:** React.js, HTML, CSS
- **Backend:** Flask (Python)
- **NLP & AI Models:** OpenAI Whisper, Hugging Face Transformers
- **Authentication:** JWT-based authentication
- **Task Management:** Celery, Redis
  
## 📂 Project Structure

QuickRecap/
│── .git/                      # Version control
│── frontend/                  # Frontend React app
│── backend/                   # Flask backend for processing
│── uploads/                   # Stores uploaded audio/text files
│── models/                    # Pre-trained NLP models
│── requirements.txt            # Backend dependencies
│── README.md                  # Project documentation
```

##  Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone <repository-url>
cd QuickRecap
```
### 2️⃣ Install Dependencies
```sh
# Frontend dependencies
cd frontend
npm install 

# Backend dependencies
cd ../backend
pip install -r requirements.txt
```
### 3️⃣ Running the Application
```sh
# Start Backend (Flask)
cd backend
python app.py

# Start Frontend (React)
cd frontend
npm start

##  Usage
1. **Upload** an audio or text file.
2. **Process** the file to generate a summary.
3. **Retrieve & download** the structured meeting summary.
4. **Analyze** extracted insights, key points, and decisions.

##  Running AI Models for Summarization
Ensure the `uploads/` directory exists before running the AI model backend.
```sh
python backend/app.py
```
The API will process the uploaded file and return structured meeting summaries.

##  License
This project is licensed under the **MIT License**.

---



