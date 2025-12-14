import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Learning Command Hub | Master Your Craft",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium Light Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
    
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    
    html, body, [class*="css"] {
        font-family: 'Outfit', -apple-system, sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }
    
    #MainMenu, footer, header, [data-testid="stSidebar"], 
    [data-testid="collapsedControl"], .stDeployButton { display: none !important; }
    
    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%) !important;
    }
    
    .block-container {
        padding: 1rem 2rem 3rem 2rem !important;
        max-width: 1400px !important;
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hero */
    .hero {
        text-align: center;
        padding: 50px 20px 40px;
    }
    
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ede9fe, #dbeafe);
        border: 1px solid #c4b5fd;
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 0.85rem;
        color: #7c3aed;
        font-weight: 600;
        margin-bottom: 25px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: clamp(2.5rem, 6vw, 4.5rem);
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 20px;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #1e293b 0%, #7c3aed 30%, #3b82f6 60%, #10b981 100%);
        background-size: 300% 300%;
        animation: gradient-shift 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.15rem;
        color: #64748b;
        max-width: 650px;
        margin: 0 auto 35px;
        line-height: 1.7;
    }
    
    /* Stats */
    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin: 40px 0;
        flex-wrap: wrap;
        background: #ffffff;
        padding: 30px 50px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }
    
    .stat-item { text-align: center; }
    
    .stat-number {
        font-family: 'Space Grotesk', monospace;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #7c3aed, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: #64748b;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-header {
        margin: 50px 0 25px;
    }
    
    .section-label {
        font-size: 0.8rem;
        color: #7c3aed;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #1e293b;
    }
    
    /* Academy Cards */
    .academy-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 20px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
    }
    
    .academy-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border-color: transparent;
    }
    
    .card-accent {
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
    }
    
    .accent-blue { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
    .accent-purple { background: linear-gradient(90deg, #8b5cf6, #a78bfa); }
    .accent-green { background: linear-gradient(90deg, #10b981, #34d399); }
    .accent-amber { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
    
    .card-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    
    .card-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
    }
    
    .icon-blue { background: #eff6ff; border: 1px solid #bfdbfe; }
    .icon-purple { background: #f5f3ff; border: 1px solid #ddd6fe; }
    .icon-green { background: #ecfdf5; border: 1px solid #a7f3d0; }
    .icon-amber { background: #fffbeb; border: 1px solid #fde68a; }
    
    .card-title-area { flex: 1; }
    
    .card-category {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 4px;
    }
    
    .cat-blue { color: #3b82f6; }
    .cat-purple { color: #8b5cf6; }
    .cat-green { color: #10b981; }
    .cat-amber { color: #f59e0b; }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
    }
    
    .card-desc {
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    
    .card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 20px;
    }
    
    .tag {
        padding: 5px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 500;
        background: #f1f5f9;
        color: #475569;
        border: 1px solid #e2e8f0;
    }
    
    .card-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 15px;
    }
    
    .card-stats {
        display: flex;
        gap: 20px;
        font-size: 0.85rem;
        color: #64748b;
    }
    
    .card-btn {
        display: inline-block;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none !important;
        color: white !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    
    .btn-blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }
    .btn-purple { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
    .btn-green { background: linear-gradient(135deg, #10b981, #059669); }
    .btn-amber { background: linear-gradient(135deg, #f59e0b, #d97706); }
    
    .card-btn:hover { transform: scale(1.05); box-shadow: 0 8px 25px rgba(0,0,0,0.2); }
    
    /* Quick Access */
    .quick-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-top: 25px;
    }
    
    .quick-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 25px 15px;
        text-align: center;
        text-decoration: none !important;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }
    
    .quick-card:hover {
        background: #f8fafc;
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-color: #c4b5fd;
    }
    
    .quick-icon { font-size: 2rem; margin-bottom: 10px; display: block; }
    .quick-title { color: #1e293b; font-weight: 600; font-size: 0.95rem; }
    .quick-sub { color: #64748b; font-size: 0.75rem; margin-top: 3px; }
    
    /* CTA Box */
    .cta-box {
        margin: 60px 0;
        padding: 50px 40px;
        background: linear-gradient(135deg, #ede9fe 0%, #dbeafe 100%);
        border: 1px solid #c4b5fd;
        border-radius: 28px;
        text-align: center;
    }
    
    .cta-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 12px;
    }
    
    .cta-text {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 25px;
    }
    
    .cta-btn {
        display: inline-block;
        padding: 14px 30px;
        background: linear-gradient(135deg, #7c3aed, #6366f1);
        border-radius: 14px;
        color: white !important;
        text-decoration: none !important;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.3);
        transition: all 0.3s ease;
    }
    
    .cta-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(124, 58, 237, 0.4);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 40px 20px;
        border-top: 1px solid #e2e8f0;
        margin-top: 40px;
        background: #ffffff;
    }
    
    .footer-brand {
        font-size: 1.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #7c3aed, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .footer-text { color: #64748b; font-size: 0.9rem; }
    .footer-link { color: #7c3aed; text-decoration: none; font-weight: 500; }
    
    @media (max-width: 768px) {
        .quick-grid { grid-template-columns: repeat(2, 1fr); }
        .stats-bar { gap: 25px; padding: 25px; }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-badge">✨ Your Learning Universe</div>
    <h1 class="hero-title">Master Your Craft</h1>
    <p class="hero-subtitle">
        One portal to rule them all. Access all your learning academies and accelerate your journey from beginner to expert.
    </p>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-bar">
    <div class="stat-item"><div class="stat-number">4+</div><div class="stat-label">Academies</div></div>
    <div class="stat-item"><div class="stat-number">150+</div><div class="stat-label">Lessons</div></div>
    <div class="stat-item"><div class="stat-number">50+</div><div class="stat-label">Projects</div></div>
    <div class="stat-item"><div class="stat-number">∞</div><div class="stat-label">Potential</div></div>
</div>
""", unsafe_allow_html=True)

# Section Header
st.markdown("""
<div class="section-header">
    <div class="section-label">Explore & Learn</div>
    <div class="section-title">Learning Academies</div>
</div>
""", unsafe_allow_html=True)

# Academy Cards
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="academy-card">
        <div class="card-accent accent-blue"></div>
        <div class="card-header">
            <div class="card-icon icon-blue">🐍</div>
            <div class="card-title-area">
                <div class="card-category cat-blue">Programming</div>
                <div class="card-title">Python Mastery</div>
            </div>
        </div>
        <p class="card-desc">From "Hello World" to Neural Networks. Master Python fundamentals, OOP, advanced concepts, and build production AI systems with PyTorch & NumPy.</p>
        <div class="card-tags">
            <span class="tag">Python 3.12+</span>
            <span class="tag">AI/ML</span>
            <span class="tag">PyTorch</span>
            <span class="tag">NumPy</span>
        </div>
        <div class="card-footer">
            <div class="card-stats">📚 40+ Lessons • ⏱️ 40 Hours</div>
            <a href="https://python-mastery.streamlit.app" target="_blank" class="card-btn btn-blue">Launch →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="academy-card">
        <div class="card-accent accent-green"></div>
        <div class="card-header">
            <div class="card-icon icon-green">🤖</div>
            <div class="card-title-area">
                <div class="card-category cat-green">Automation</div>
                <div class="card-title">Automation Testing Academy</div>
            </div>
        </div>
        <p class="card-desc">Master modern test automation frameworks used by top tech companies. Build robust, maintainable test suites that catch bugs before production.</p>
        <div class="card-tags">
            <span class="tag">Playwright</span>
            <span class="tag">WebdriverIO</span>
            <span class="tag">Karate</span>
            <span class="tag">CI/CD</span>
        </div>
        <div class="card-footer">
            <div class="card-stats">📚 45+ Lessons • ⏱️ 35 Hours</div>
            <a href="https://automation-testing-academy.streamlit.app" target="_blank" class="card-btn btn-green">Launch →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="academy-card">
        <div class="card-accent accent-purple"></div>
        <div class="card-header">
            <div class="card-icon icon-purple">⚡</div>
            <div class="card-title-area">
                <div class="card-category cat-purple">Testing</div>
                <div class="card-title">Performance Testing Academy</div>
            </div>
        </div>
        <p class="card-desc">Expert-level performance testing with industry tools. Learn to identify bottlenecks, optimize systems, and ensure applications scale under load.</p>
        <div class="card-tags">
            <span class="tag">JMeter</span>
            <span class="tag">k6</span>
            <span class="tag">Gatling</span>
            <span class="tag">Locust</span>
        </div>
        <div class="card-footer">
            <div class="card-stats">📚 35+ Lessons • ⏱️ 30 Hours</div>
            <a href="https://performance-testing.streamlit.app" target="_blank" class="card-btn btn-purple">Launch →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="academy-card">
        <div class="card-accent accent-amber"></div>
        <div class="card-header">
            <div class="card-icon icon-amber">🧠</div>
            <div class="card-title-area">
                <div class="card-category cat-amber">AI & Machine Learning</div>
                <div class="card-title">Learn Artificial Intelligence</div>
            </div>
        </div>
        <p class="card-desc">Master AI fundamentals, neural networks, and machine learning. From basics to building production-ready AI systems with hands-on projects.</p>
        <div class="card-tags">
            <span class="tag">AI/ML</span>
            <span class="tag">Neural Networks</span>
            <span class="tag">Deep Learning</span>
            <span class="tag">LLMs</span>
        </div>
        <div class="card-footer">
            <div class="card-stats">📚 50+ Lessons • ⏱️ 45 Hours</div>
            <a href="https://learn-artificial-intelligence.streamlit.app" target="_blank" class="card-btn btn-amber">Launch →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick Access
st.markdown("""
<div class="section-header">
    <div class="section-label">Jump Right In</div>
    <div class="section-title">Quick Access</div>
</div>
<div class="quick-grid">
    <a href="https://python-mastery.streamlit.app/Beginner" target="_blank" class="quick-card">
        <span class="quick-icon">🎯</span>
        <div class="quick-title">Start Python</div>
        <div class="quick-sub">Beginner Module</div>
    </a>
    <a href="https://automation-testing-academy.streamlit.app" target="_blank" class="quick-card">
        <span class="quick-icon">🧪</span>
        <div class="quick-title">API Testing</div>
        <div class="quick-sub">REST & GraphQL</div>
    </a>
    <a href="https://performance-testing.streamlit.app" target="_blank" class="quick-card">
        <span class="quick-icon">📊</span>
        <div class="quick-title">Load Testing</div>
        <div class="quick-sub">JMeter & k6</div>
    </a>
    <a href="https://learn-artificial-intelligence.streamlit.app" target="_blank" class="quick-card">
        <span class="quick-icon">🧠</span>
        <div class="quick-title">AI & ML</div>
        <div class="quick-sub">Neural Networks</div>
    </a>
</div>
""", unsafe_allow_html=True)

# CTA
st.markdown("""
<div class="cta-box">
    <div class="cta-title">🚀 Ready to Level Up?</div>
    <p class="cta-text">Start your learning journey today. All academies are free and continuously updated.</p>
    <a href="https://python-mastery.streamlit.app" target="_blank" class="cta-btn">Begin with Python →</a>
</div>
""", unsafe_allow_html=True)

# Footer
current_year = datetime.now().year
st.markdown(f"""
<div class="footer">
    <div class="footer-brand">Learning Command Hub</div>
    <p class="footer-text">
        © {current_year} All rights reserved. Created with ❤️ by 
        <a href="mailto:vikas.singh.info@gmail.com" class="footer-link">vikas.singh.info@gmail.com</a>
    </p>
</div>
""", unsafe_allow_html=True)
