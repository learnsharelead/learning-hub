import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Learning Command Hub | Master Your Craft",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SEO and Social Media Meta Tags
st.markdown("""
<!-- Primary Meta Tags -->
<title>Learning Command Hub | Master Your Craft</title>
<meta name="title" content="Learning Command Hub | Master Your Craft">
<meta name="description" content="One portal to rule them all. Access all your learning academies: Python, Automation, Performance, and AI.">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://learning-command-hub.streamlit.app/">
<meta property="og:title" content="Learning Command Hub | Master Your Craft">
<meta property="og:description" content="One portal to rule them all. Access all your learning academies: Python, Automation, Performance, and AI.">
<meta property="og:image" content="https://raw.githubusercontent.com/learnsharelead/learning-hub/main/static/screenshot-1.png">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://learning-command-hub.streamlit.app/">
<meta property="twitter:title" content="Learning Command Hub | Master Your Craft">
<meta property="twitter:description" content="One portal to rule them all. Access all your learning academies: Python, Automation, Performance, and AI.">
<meta property="twitter:image" content="https://raw.githubusercontent.com/learnsharelead/learning-hub/main/static/screenshot-1.png">

<!-- PWA and Mobile Tags -->
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="LearnHub">
<meta name="application-name" content="Learning Command Hub">
<meta name="theme-color" content="#7c3aed">
<meta name="msapplication-TileColor" content="#7c3aed">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5, user-scalable=yes">
<link rel="manifest" href="https://raw.githubusercontent.com/learnsharelead/learning-hub/main/static/manifest.json">
<link rel="apple-touch-icon" href="https://raw.githubusercontent.com/learnsharelead/learning-hub/main/static/icon-192.png">
""", unsafe_allow_html=True)

# Premium Compact Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif !important;
    }
    
    #MainMenu, footer, header, [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
    
    .stApp {
        background: #f8fafc !important;
    }
    
    .block-container {
        padding: 1.5rem 2rem !important;
        max-width: 100% !important;
    }
    
    /* Compact Hero */
    .hero-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px solid #e2e8f0;
    }
    
    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #7c3aed, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    
    .hero-subtitle {
        color: #64748b;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Compact Card */
    .academy-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        height: 100%;
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
    }
    
    .academy-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-color: #cbd5e1;
    }
    
    .card-top {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    
    .card-icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    
    .icon-blue { background: #eff6ff; color: #3b82f6; }
    .icon-green { background: #ecfdf5; color: #10b981; }
    .icon-purple { background: #f5f3ff; color: #8b5cf6; }
    .icon-amber { background: #fffbeb; color: #f59e0b; }
    
    .card-title {
        font-size: 1rem;
        font-weight: 700;
        color: #1e293b;
        line-height: 1.2;
    }
    
    .card-desc {
        font-size: 0.8rem;
        color: #64748b;
        line-height: 1.4;
        margin-bottom: 12px;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        height: 36px; /* Fixed height for consistency */
    }
    
    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: auto;
    }
    
    .tag {
        font-size: 0.7rem;
        color: #94a3b8;
        background: #f1f5f9;
        padding: 2px 8px;
        border-radius: 4px;
    }
    
    .launch-link {
        font-size: 0.8rem;
        font-weight: 600;
        color: #7c3aed !important;
        text-decoration: none !important;
        padding: 4px 10px;
        border-radius: 6px;
        background: #f5f3ff;
        transition: all 0.2s;
    }
    
    .launch-link:hover {
        background: #7c3aed;
        color: white !important;
    }
    
    .footer-compact {
        text-align: center;
        font-size: 0.75rem;
        color: #94a3b8;
        margin-top: 25px;
        border-top: 1px solid #e2e8f0;
        padding-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Compact Header
st.markdown("""
<div class="hero-container">
    <div>
        <h1 class="hero-title">Learning Command Hub</h1>
        <p class="hero-subtitle">Master Your Craft • Access all academies from one central dashboard</p>
    </div>
    <div style="text-align: right; font-size: 0.8rem; color: #64748b;">
        <div><b>8</b> Powered Apps</div>
        <div><b>24/7</b> Availability</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Grid Layout: 4 Columns
col1, col2, col3, col4 = st.columns(4)

# Column 1
with col1:
    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-blue">🐍</div>
            <div class="card-title">Python Mastery</div>
        </div>
        <p class="card-desc">Master Python fundamentals to advanced AI systems with PyTorch.</p>
        <div class="card-footer">
            <span class="tag">AI/ML</span>
            <a href="https://python-mastery.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-purple">⚡</div>
            <div class="card-title">Performance Testing</div>
        </div>
        <p class="card-desc">Optimize systems with JMeter, k6, and Gatling at expert level.</p>
        <div class="card-footer">
            <span class="tag">Testing</span>
            <a href="https://performance-testing.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Column 2
with col2:
    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-green">🤖</div>
            <div class="card-title">Automation Academy</div>
        </div>
        <p class="card-desc">Build robust test suites with Playwright and WebdriverIO.</p>
        <div class="card-footer">
            <span class="tag">Automation</span>
            <a href="https://automation-testing-academy.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-amber">🧠</div>
            <div class="card-title">Learn AI & ML</div>
        </div>
        <p class="card-desc">From basics to production-ready AI systems and Neural Networks.</p>
        <div class="card-footer">
            <span class="tag">Deep Learning</span>
            <a href="https://learn-artificial-intelligence.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Column 3
with col3:
    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-green">💰</div>
            <div class="card-title">AI Finance</div>
        </div>
        <p class="card-desc">Smart market analysis and investment insights powered by AI.</p>
        <div class="card-footer">
            <span class="tag">Finance</span>
            <a href="https://ai-finance.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-amber">🔍</div>
            <div class="card-title">AI Model Hunter</div>
        </div>
        <p class="card-desc">Discover and compare the best AI models for your use case.</p>
        <div class="card-footer">
            <span class="tag">Discovery</span>
            <a href="https://ai-model-hunter.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Column 4
with col4:
    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-purple">👩‍🏫</div>
            <div class="card-title">Coach Sushma</div>
        </div>
        <p class="card-desc">Your personal AI coach for career growth and interview prep.</p>
        <div class="card-footer">
            <span class="tag">Career</span>
            <a href="https://coach-sushma.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="academy-card">
        <div class="card-top">
            <div class="card-icon icon-blue">🌐</div>
            <div class="card-title">Website AI Agent</div>
        </div>
        <p class="card-desc">Intelligent agent for web scraping and content analysis.</p>
        <div class="card-footer">
            <span class="tag">Agent</span>
            <a href="https://website-ai-agent.streamlit.app" target="_blank" class="launch-link">Launch ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Compact Footer
current_year = datetime.now().year
st.markdown(f"""
<div class="footer-compact">
    © {current_year} Learning Command Hub • <a href="mailto:vikas.singh.info@gmail.com" style="color: #94a3b8; text-decoration: none;">Contact Support</a>
</div>
""", unsafe_allow_html=True)
