# 🎨 Story Sketch AI  
**An AI-powered storytelling app that listens to your audio, transcribes your story, and generates creative scene-by-scene visualizations.**

---

## 🧠 Project Overview
**Story Sketch AI** transforms spoken ideas into engaging story outlines and scene summaries using **speech-to-text transcription** and **generative AI**.  
It provides an intuitive Streamlit interface for creators, writers, and educators to narrate stories and instantly visualize the results.

---

## 🚀 Features

### 🗣️ Audio-to-Story
- Record or upload your voice narration  
- Transcription powered by **Groq** (Whisper-like ASR)  
- Real-time text output and scene extraction

### ✍️ Intelligent Story Generation
- Automatically identifies story structure and themes  
- Extracts key **scenes, emotions, and settings**  
- Generates detailed story summaries or creative outlines

### 🎨 Interactive Streamlit UI
- Clean and responsive interface with progress indicators  
- Tabs for **Recording**, **Generated Story**, and **Scene Insights**  
- Visual progress and success highlights for better UX

### ⚙️ Improved Functionality
| Area | Issue | Fix |
|------|--------|-----|
| `main.py` | UI state reset (story regenerates unnecessarily) | Implemented `st.session_state` for stable state control |
| `audio_recorder_streamlit` | Audio buffer not exporting properly on Streamlit Cloud | Used direct `bytes` handling |
| `groq` transcription | Missing validation and error catch | Added error handling for invalid/missing audio |
| `generate_story` / `extract_scenes` | Silent failures | Added informative exception messages |
| Streamlit Deploy | Relative import issues | Adjusted to Cloud-safe imports |
| UX | Basic and plain | Added tabs, progress indicators, and color highlights |

---

## 🧩 Project Structure
```
StorySketchAI/
│
├── main.py                     # Streamlit app with UI and logic
├── utils/
│   ├── transcription.py        # Groq/Whisper transcription logic
│   ├── story_generation.py     # GPT-based story and scene generation
│   └── helpers.py              # Utility functions for validation and I/O
├── assets/
│   ├── logo.png                # App logo or banner
│   ├── demo_screenshot.png     # App preview image
│   └── audio_samples/          # Optional example recordings
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/<your-username>/StorySketchAI.git
cd StorySketchAI
```

### **2️⃣ Install Requirements**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the App**
```bash
streamlit run main.py
```

> Make sure your `.env` file contains valid API keys for **Groq** (or OpenAI-compatible) and any LLM provider used.

---

## 🧱 Core Components

### 🎙️ `audio_recorder_streamlit`
- Custom audio recorder widget for Streamlit  
- Improved for browser and Streamlit Cloud compatibility

### 🧩 `groq` Transcription
- Converts user-recorded audio to text  
- Handles invalid files and empty buffers gracefully

### 🪄 `generate_story`
- Processes the transcribed text into story structure  
- Uses LLM to summarize and extract main scenes, emotions, and tone

### 🖼️ `extract_scenes`
- Breaks down the generated story into visually descriptive “scene cards”  
- Each card contains setting, characters, and core emotion

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend UI | Streamlit |
| Backend Logic | Python |
| AI/LLM | Groq API / GPT Model |
| Audio Processing | `audio_recorder_streamlit` |
| Environment | `.env`, Streamlit Cloud Ready |

---

## 💡 Key Improvements

- ✅ Added **`st.session_state`** to maintain app state across interactions  
- ✅ Integrated **audio validation** and **robust exception handling**  
- ✅ Enhanced **UX/UI** with modern layout, tabs, and color feedback  
- ✅ Streamlit Cloud–safe imports for deployment  
- ✅ Modularized code for readability and scalability  

---

## 🖼️ Preview
*(Add your screenshot or demo GIF here)*  
![App Demo](assets/demo_screenshot.png)

---

## 📈 Future Enhancements
- 🧍 Character name extraction and consistency tracking  
- 🎬 Scene image generation using text-to-image AI  
- 📜 Downloadable story summary as PDF  
- 🌐 Multi-language story narration support  

---

## 🤝 Contributing
We welcome community contributions!

### **How to Contribute**
```bash
# 1️⃣ Fork the repository
# 2️⃣ Create a new feature branch
git checkout -b feature/AmazingFeature

# 3️⃣ Make your changes
# 4️⃣ Commit your work
git commit -m 'Add some AmazingFeature'

# 5️⃣ Push and open a Pull Request
git push origin feature/AmazingFeature
```

---

⭐ **If you found this project helpful, please give it a star!**  
Built with ❤️ using **Python**, **Streamlit**, and **AI**.
