import streamlit as st
import sys
import os

sys.path.append(os.getcwd())

from config.apps_config import APPS
from components.app_card import render_app_card
from components.filters import render_filters
from utils.styling import load_custom_css

# Compact Layout
st.set_page_config(
    page_title="Learning Hub",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(load_custom_css(), unsafe_allow_html=True)

# HEADER
st.markdown('<div class="gradient-text">Learning Hub</div>', unsafe_allow_html=True)
st.markdown("**Your colorful workspace for knowledge & tools.**")

st.write("")

# FILTERS (Hidden in sidebar by default to save space)
filters = render_filters()
search_query = filters["search_query"]
selected_categories = filters["selected_categories"]
selected_difficulty = filters["selected_difficulty"]
sort_option = filters["sort_option"]
show_active = filters["show_featured_only"]

# LOGIC
filtered = APPS.copy()
if search_query:
    q = search_query.lower()
    filtered = [a for a in filtered if q in a['name'].lower() or q in a['description'].lower()]
if selected_categories:
    filtered = [a for a in filtered if a['category'] in selected_categories]
if selected_difficulty != "All":
    filtered = [a for a in filtered if a['difficulty'] == selected_difficulty]
if show_active:
    filtered = [a for a in filtered if a.get('featured')]

if sort_option == "Newest First":
    filtered.sort(key=lambda x: x['date_added'], reverse=True)
elif sort_option == "A to Z":
    filtered.sort(key=lambda x: x['name'])
elif sort_option == "Category":
    filtered.sort(key=lambda x: x['category'])

# --- COMPACT GRID (4 COLUMNS) ---
if not filtered:
    st.warning("No apps found.")
else:
    # Use 4 columns for compact desktop view
    # On mobile, Streamlit handles responsiveness automatically (stacks to 1)
    
    COLS = 4 
    cols = st.columns(COLS)
    
    for i, app in enumerate(filtered):
        with cols[i % COLS]:
            render_app_card(app, key_suffix=f"_{i}")
            
# Footer
st.divider()
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>© 2025 Learning Hub (Compact Edition)</div>", unsafe_allow_html=True)
