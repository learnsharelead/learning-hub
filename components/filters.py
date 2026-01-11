import streamlit as st
from config.apps_config import APPS

def render_filters():
    """Render clean, functional sidebar filters."""
    
    with st.sidebar:
        st.header("🔍 Filters")
        
        # Search
        search_query = st.text_input("Search apps...", placeholder="Type to search", key="search_bar")
        
        st.write("---")
        
        # Category filter
        st.subheader("📁 Category")
        all_categories = sorted(set(app['category'] for app in APPS))
        selected_categories = st.multiselect(
            "Select Categories",
            all_categories,
            default=[],
        )
        
        st.write("---")
        
        # Difficulty
        st.subheader("📊 Difficulty")
        difficulty_levels = ["All", "Beginner", "Intermediate", "Advanced"]
        selected_difficulty = st.selectbox(
            "Select Level",
            difficulty_levels,
        )
        
        st.write("---")
        
        # Sort
        st.subheader("🔃 Sort By")
        sort_options = ["Category", "Newest First", "Most Popular", "A to Z"]
        sort_option = st.selectbox(
            "Sort Order",
            sort_options,
        )
        
        # Featured toggle
        st.write("")
        show_featured_only = st.toggle("⭐ Show Featured Only")
        
        # Reset
        if st.button("Reset Filters", type="primary", use_container_width=True):
             st.rerun()

    return {
        "search_query": search_query,
        "selected_categories": selected_categories,
        "selected_difficulty": selected_difficulty,
        "sort_option": sort_option,
        "show_featured_only": show_featured_only
    }
