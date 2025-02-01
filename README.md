# 🎯 Research Paper Visualization Tool

> Transform research papers into visually appealing graphical abstracts using AI.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

* 📄 **PDF Processing** - Automatically extract key information from research papers
* 🎨 **AI-Powered Visualization** - Generate beautiful graphical abstracts using DALL-E
* 💫 **Interactive UI** - Modern, responsive interface with Gen-Z aesthetic
* 🚀 **Batch Processing** - Handle multiple papers simultaneously
* 🎭 **Custom Styling** - Personalize the output with different themes and layouts
* 💾 **Export Options** - Download visuals in various formats

## 🔧 Prerequisites

* Python 3.9 or higher
* Node.js 14+ (for some UI components)
* GPU recommended for faster processing
* Internet connection for API access

## ⚡️ Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/research-paper-visualization.git
cd research-paper-visualization
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys and configurations
```

## 🏃‍♂️ Running the Application

1. **Start the backend server**
```bash
python backend/process_pdfs.py
```

2. **Launch the frontend**
## Quick Start
u can access the published site at: https://v0-min-ed-hackathon-djnguy.vercel.app/



3. **Access the application at** `http://localhost:8501`

## 📁 Project Structure

```
📦 Project_Name/
│
├── 📂 input_pdfs/         # Users upload PDFs here
│
├── 📂 output/             # Processed summaries & images
│   ├── 📂 Paper_1/        # Folder for each research paper
│   │   ├── summary.json   # Text summary of the paper
│   │   ├── summary.png    # Graphical representation
│   ├── 📂 Paper_2/        
│
├── 📂 backend/            # Backend logic
│   ├── 📂 MINED-HACKATHON/
│   ├── text_extraction.py
│   ├── summarization.py
│   ├── image_generator.py
│   └── process_pdfs.py
│
├── 📂 frontend/           # UI components (Streamlit)
│   ├── app.py            # Main Streamlit application
│   ├── templates/        # HTML templates
│   └── static/           # CSS/JS files
│
├── requirements.txt      # Project dependencies
└── README.md            # You are here! 😊
```

## 🎯 Usage Guide

### 1. Upload Papers
- Drag and drop PDFs into the upload area
- Select multiple files for batch processing
- Supports most academic paper formats

### 2. Processing
- System automatically extracts key information
- Generates visual summaries using AI
- Shows real-time progress with status updates

### 3. Customization
- Choose from multiple visual themes
- Adjust layout options
- Modify text placement and styling
- Select color schemes

### 4. Export
- Download generated images in various formats
- Export summaries as JSON
- Share results directly via link

## ⚙️ Configuration

Configuration options in `.env`:

```env
OPENAI_API_KEY=your_key_here
MAX_CONCURRENT_PROCESSES=4
OUTPUT_DIRECTORY=./output
DEBUG_MODE=False
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

## 🐛 Common Issues & Solutions

### Installation Problems
- Ensure Python version compatibility (3.9+)
- Check virtual environment activation
- Verify all dependencies are installed correctly

### Processing Errors
- Confirm PDF format is supported
- Check API key validity
- Verify internet connection is stable

### Performance Issues
- Reduce concurrent processing in settings
- Check system resources availability
- Clear application cache

## 📮 Support

- 📧 Email: support@example.com
- 💬 Discord: [Join our server](https://discord.gg/example)
- 📚 Documentation: [Read the docs](https://docs.example.com)

## 🛣️ Roadmap

- [ ] Support for more paper formats
- [ ] Advanced customization options
- [ ] Batch export features
- [ ] Integration with additional AI models
- [ ] Collaboration features
- [ ] API access for developers

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

* OpenAI for DALL-E API
* Streamlit team for the amazing framework
* All contributors and testers

---

<div align="center">
Made with ❤️ by She++<br>
If you found this project helpful, please consider giving it a ⭐
</div>
