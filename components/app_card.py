import streamlit as st
from config.apps_config import CATEGORY_COLORS

def render_app_card(app_data, key_suffix=""):
    """
    Render a compact, colorful native card.
    """
    
    # Get color
    color = CATEGORY_COLORS.get(app_data['category'], "#6366f1")
    
    with st.container(border=True):
        # Compact Header: Icon + Name
        # We use columns to tighten spacing
        c1, c2 = st.columns([1, 4])
        with c1:
            st.markdown(f"<div style='font-size: 1.5rem;'>{app_data['icon']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div style='font-weight: 700; font-size: 1rem; line-height: 1.2; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{app_data['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='color: {color}; font-size: 0.75rem; font-weight: 600; text-transform: uppercase;'>{app_data['category']}</div>", unsafe_allow_html=True)

        st.markdown(f"<div style='font-size: 0.8rem; color: #64748b; height: 40px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; margin-top: 8px; margin-bottom: 8px;'>{app_data['description']}</div>", unsafe_allow_html=True)
        
        # Tech Stack - Tiny pills
        # Limit to 2 items for compactness
        techs = app_data['tech_stack'][:2]
        st.caption(" ".join([f"`{t}`" for t in techs]))
        
        # Buttons
        b1, b2 = st.columns(2)
        launch_url = app_data['launch_url']
        is_external = launch_url.startswith('http')
        
        with b1:
            if is_external:
                st.link_button("🚀 Open", launch_url, type="primary", use_container_width=True)
            else:
                if st.button("🚀 Open", key=f"launch_{app_data['id']}{key_suffix}", type="primary", use_container_width=True):
                    st.switch_page(launch_url)
        with b2:
             if st.button("ℹ️ Info", key=f"details_{app_data['id']}{key_suffix}", use_container_width=True):
                 from components.modal import show_details_modal
                 show_details_modal(app_data)
