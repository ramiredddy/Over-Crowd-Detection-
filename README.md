# Over-Crowd-Detection

A computer vision-based system for detecting and monitoring crowd density in real-time using deep learning techniques. This project helps analyze crowd patterns and identify potential overcrowding situations in public spaces, events, or surveillance scenarios.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)
- [Example Outputs](#example-outputs)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Over-Crowd Detection system leverages computer vision and machine learning algorithms to automatically detect and analyze crowd density in video feeds or images. This tool is designed to assist security personnel, event managers, and public safety officials in monitoring crowd levels and taking proactive measures to prevent overcrowding incidents.

### Key Objectives
- Real-time crowd density estimation
- Automated alert generation for overcrowding situations
- Visual representation of crowd distribution
- Scalable solution for various venue types and sizes

### Technology Stack
- **Python**: Core programming language
- **Deep Learning Frameworks**: TensorFlow/PyTorch for crowd detection models
- **Computer Vision**: OpenCV for image/video processing
- **Web Framework**: Flask/FastAPI for application interface

## Features

- ✅ **Real-time Detection**: Process live video streams or recorded footage
- ✅ **Crowd Density Estimation**: Calculate the number of people in a given area
- ✅ **Heatmap Visualization**: Visual representation of crowd concentration
- ✅ **Alert System**: Configurable thresholds for overcrowding alerts
- ✅ **Multi-camera Support**: Handle multiple video sources simultaneously
- ✅ **Historical Analysis**: Store and analyze crowd patterns over time
- ✅ **User-friendly Interface**: Web-based dashboard for monitoring
- ✅ **Export Reports**: Generate crowd analytics reports in various formats

## Installation

### Prerequisites

Before installing, ensure you have the following:
- Python 3.8 or higher
- pip (Python package manager)
- Git
- (Optional) CUDA-compatible GPU for faster processing

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ramiredddy/Over-Crowd-Detection-.git
   cd Over-Crowd-Detection-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download pre-trained models** (if applicable)
   ```bash
   # Follow instructions in models/ directory
   # Or the models will be downloaded automatically on first run
   ```

5. **Verify installation**
   ```bash
   python app.py --help
   ```

## Usage Guide

### Basic Usage

**1. Running the Web Application**
```bash
python app.py
```
Then open your browser and navigate to `http://localhost:5000`

**2. Processing a Video File**
```bash
python app.py --input path/to/video.mp4 --output results/
```

**3. Real-time Camera Feed**
```bash
python app.py --source camera --camera-id 0
```

### Configuration

Edit the configuration file or pass parameters:

```bash
python app.py --threshold 50 --alert-email admin@example.com
```

**Available Parameters:**
- `--input`: Path to input video file
- `--output`: Directory for output results
- `--threshold`: Crowd density threshold for alerts (default: 50)
- `--source`: Input source type (video/camera/stream)
- `--camera-id`: Camera device ID for live feed
- `--model`: Path to custom trained model
- `--visualize`: Enable visualization overlay

### Advanced Usage

**Using Custom Models**
```python
from models import CrowdDetector

detector = CrowdDetector(model_path='path/to/custom_model.pth')
results = detector.detect(image_path='crowd_image.jpg')
print(f"Detected crowd count: {results['count']}")
```

## File Structure

```
Over-Crowd-Detection-/
│
├── app.py                  # Main application entry point
├── models.py              # Model definitions and detection logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── TODO.md               # Development roadmap and tasks
│
├── models/               # Pre-trained models directory
│   ├── yolo_weights.pt
│   └── crowd_model.h5
│
├── static/               # Static assets for web interface
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/            # HTML templates
│   ├── index.html
│   └── dashboard.html
│
├── utils/                # Utility functions
│   ├── preprocessing.py
│   ├── postprocessing.py
│   └── visualization.py
│
├── data/                 # Sample data and test videos
│   ├── samples/
│   └── test_videos/
│
└── results/              # Output directory for results
    ├── videos/
    ├── reports/
    └── logs/
```

## Example Outputs

### Console Output
```
[2025-10-30 21:08:00] INFO: Crowd Detection Started
[2025-10-30 21:08:02] INFO: Processing frame 1/1000
[2025-10-30 21:08:02] INFO: Detected: 45 people
[2025-10-30 21:08:03] WARNING: Crowd density threshold reached: 52 people
[2025-10-30 21:08:03] ALERT: Overcrowding detected!
```

### Sample Visualization

The system generates:
- **Annotated videos** with bounding boxes around detected individuals
- **Heatmaps** showing crowd density distribution
- **Graphs** displaying crowd count over time
- **Reports** in JSON/CSV format with detailed statistics

### Sample Output Data
```json
{
  "timestamp": "2025-10-30T21:08:00Z",
  "frame_id": 150,
  "crowd_count": 52,
  "density_level": "high",
  "alert_triggered": true,
  "regions": [
    {"area": "entrance", "count": 30},
    {"area": "main_hall", "count": 22}
  ]
}
```

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the repository**
   - Click the 'Fork' button at the top right of this page

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Over-Crowd-Detection-.git
   cd Over-Crowd-Detection-
   ```

3. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow PEP 8 style guidelines for Python
   - Add tests if applicable

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click 'New Pull Request'
   - Select your fork and branch
   - Describe your changes clearly

### Contribution Guidelines

- **Code Quality**: Ensure your code is well-documented and follows Python best practices
- **Testing**: Add unit tests for new features
- **Documentation**: Update README.md if you change functionality
- **Issues**: Check existing issues before creating new ones
- **Communication**: Be respectful and constructive in discussions

### Areas for Contribution

- 🐛 Bug fixes and issue resolution
- ✨ New features and enhancements
- 📝 Documentation improvements
- 🧪 Test coverage expansion
- 🎨 UI/UX improvements
- 🌐 Localization and translations
- ⚡ Performance optimizations

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code style
flake8 .

# Format code
black .
```

## License

This project is licensed under the **MIT License** - see below for details.

### MIT License

```
MIT License

Copyright (c) 2025 ramiredddy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Support

If you encounter any issues or have questions:
- 📧 Open an issue on GitHub
- 💬 Start a discussion in the Discussions tab
- 📖 Check the documentation and TODO.md for known limitations

## Acknowledgments

- Thanks to all contributors who have helped improve this project
- Built with open-source tools and libraries
- Inspired by the need for safer public spaces

---

**Note**: This project is under active development. Check TODO.md for planned features and improvements.

**Happy Crowd Monitoring! 🎯👥**
