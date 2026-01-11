import streamlit as st

@st.cache_data
def load_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* VIBRANT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        background-attachment: fixed;
    }
    
    /* COLORFUL HEADER */
    .gradient-text {
        background: linear-gradient(to right, #2563eb, #9333ea, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
    }
    
    /* Metric styling */
    div[data-testid="stMetricValue"] {
        background: linear-gradient(45deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    
    /* Card Hover Effect */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        transition: all 0.3s ease;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
        border-color: #a78bfa !important; /* Light purple border on hover */
    }
    
    /* Button Styling */
    div.stButton > button {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: 0.2s;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
    }
    
    /* Primary buttons gradient */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 95% !important; /* Use more screen width for 4 cols */
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """
