# Unified Learning Hub 🚀

> **Your World-Class Learning Portal** — A professional hub to showcase and navigate all your Streamlit applications.

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Overview

The **Unified Learning Hub** is a visually stunning, highly interactive portal designed to centralize all your learning resources and applications. Built with a "Dark Mode First" philosophy and modern Glassmorphism aesthetics, it serves as both a navigation center and a showcase of your work.

## ✨ Key Features

- **🎨 Modern Design**: Professional dark theme, glassmorphism, and smooth animations.
- **🔍 Smart Search & Filtering**: Real-time search by name, tag, or description. Filter by category, difficulty, or sort by various metrics.
- **📱 Responsive Layout**: Adaptive grid system that looks great on all devices.
- **⚡ Performance Optimized**: Fast loading with caching and optimized assets.
- **ℹ️ Rich App Details**: Detailed modals with descriptions, tech stacks, and usage guides.

## 📚 App Collection

Access a wide range of apps including:
- **Interactive Data Explorer** (Data Science)
- **Python Mastery** (Education)
- **Performance Testing** (Utilities)
- **Automation Academy** (Education)
- **Learn AI & ML** (ML/AI)
- And many more!

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Streamlit 1.34+

### Installation

```bash
# Clone the repository
git clone https://github.com/learnsharelead/learning-hub.git
cd learning-hub

# Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run Home.py
```

## 📁 Project Structure

```
learning_hub/
├── Home.py                      # Main hub application
├── config/
│   └── apps_config.py         # App definitions and configuration
├── components/
│   ├── app_card.py           # App card component
│   ├── filters.py            # Sidebar filters
│   └── modal.py              # Details modal
├── utils/
│   ├── data_manager.py       # Data management utilities
│   └── styling.py            # Custom CSS and styling
├── assets/                   # Static assets (icons, thumbnails)
└── apps/                      # Internal apps directory
```

## 🛠️ Configuration

To add new apps, simply edit `config/apps_config.py`. Add a new dictionary entry to the `APPS` list with your app's details.

```python
{
    "id": "my_new_app",
    "name": "My New App",
    "category": "Utilities",
    ...
}
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Created with ❤️ by [vikas.singh.info@gmail.com](mailto:vikas.singh.info@gmail.com)**
